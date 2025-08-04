from data import sf_data
from data import molar_masses
import numpy as np


AVOGADRO = 6.02214076e23

class Material:
    """A class to estimate the spontaneous fission
    
    The material can be defined using atomic fractions or number densities, along
    with a total density and (optionally) a volume.

    Attributes:
        nuclides (list[str]): List of nuclide names (e.g., "U235").
        atomic_fractions (list[float]): List of atomic fractions or absolute number densities.
        density (float): Density of the material in g/cm³ or  kg/m3.
        unit (str): Unit of the density (e.g., "g/cm3").
        volume (float or None): Volume in cm³. If None, rate is returned per cm³.
        fraction (bool): Default is True then it is assumedthe the atomic_fractions will consist of atomic fractions, otherwise number densities.
    """

    def __init__(self):
        """Initializes an empty Material object."""
        self.nuclides = []
        self.atomic_fractions = []
        self.density = 0
        # self.unit = ''
        self.volume = None
        self.absolute = False

    def add_nuclide(self, name:str, atomic_fraction:float):
        """
        Method to add nuclides and its atomic fraction or number densities

        Parameters
        ------------
        name: str
            The name of the istope, eg U235
        atomic_fraction: float
            The atomic fraction or the number density
        fraction: bool
            If true (default) it assumes atomics fractions is used, if false it assumes number densities is used
        """
        self.nuclides.append(name)
        self.atomic_fractions.append(atomic_fraction)

    def set_density(self, density:float, unit:str = 'g/cm3'):
        """
        Method to set the density

        Parameters
        ------------
        density: float
            The numerical value of the density
        unit: str
            The unit of the density, g/cm3 (default) or kg/m3
        """
        if unit == 'g/cm3':
            # self.unit = unit
            self.density = density
        elif unit == 'kg/m3':
            self.density = density*0.01**3/1000 #Converting to g/cm3
        else:
            raise Exception('Unsupported density unit, please select g/cm3 (default) or kg/m3')
    
    def set_volume(self, volume:float, unit:str = 'cm3'):
        """
        Method to set the volume (optional)

        Parameters
        ------------
        volume: float
            The numerical value of the volume
        unit: str
            The unit of the volume, cm3 (default) or m3
        """
        if unit == 'cm3':
            self.volume = volume
        elif unit == 'm3':
            self.volume = volume*0.01**3 #Converting to cm3
        else:
            raise Exception('Unsupported volume unit, please select cm3 (default) or m3')

    def set_absolute(self, absolute: bool):
        """
        Method to enable absolute units (number densities) (optional)

        Parameters
        ------------
        absolute: bool
            True if number densities should be used or atmic fractions otherwise (default)
        """
        self.absolute = absolute

    def get_sf(self):
        """
        Method to estimate spontaneous fission

        returns
        ------------
        float: Spontaneous fission rate in fissions/s if volume is given,
                otherwise in fissions/s/cm³.
        """
        total_fraction = sum(self.atomic_fractions)
        sf_tot = 0
        if self.absolute == False:
            for i, nuclide in enumerate(self.nuclides):
                if nuclide not in sf_data:
                    print(f"Warning: No data for {nuclide}, skipping.")
                    continue

                half_life = sf_data[nuclide]['half_life']
                Pi = sf_data[nuclide]['sf_branching_ratio'] * 0.01 # To get in fractions instead of %

                frac = self.atomic_fractions[i] / total_fraction

                Lambda = np.log(2) / half_life
                molar_mass = molar_masses[nuclide]
                number_density = (self.density / molar_mass) * AVOGADRO * frac  # atoms/cm³

                sf = number_density * Lambda * Pi
                sf_tot += sf
        else:
            for i, nuclide in enumerate(self.nuclides):
                if nuclide not in sf_data:
                    print(f"Warning: No data for {nuclide}, skipping.")
                    continue

                half_life = sf_data[nuclide]['half_life']
                Pi = sf_data[nuclide]['sf_branching_ratio'] * 0.01 # To get in fractions instead of %

                Lambda = np.log(2) / half_life

                number_density = self.atomic_fractions[i] * 1e24

                sf = number_density * Lambda * Pi
                sf_tot += sf

        if self.volume == None:
            return sf_tot  # fissions/s/cm³
        else:
            return sf_tot * self.volume  # fissions/s
        
    def add_nuclide_data(self, name:str, half_life:int, sf_branching_ratio:float):
        """
        Method to add a new nuclide half time and spontaneous fission data

        Parameters
        ------------
        name: str
            The name of the nuclide
        half_life: int
            The half life of the nuclide in seconds
        sf_branching_ratio: float
            The spontaneous fission branching ratio for the nuclide
        """
        sf_data[name] = {'half_life':half_life, 
                         'sf_branching_ratio':sf_branching_ratio}

    def add_molar_mass(self, name:str, M:float):
        """
        Method to add a new nuclides molar mass
        Parameters
        ------------
        name: str
            The name of the nuclide
        M: float
            The molar mass of the nuclide in g/mol
        """
        molar_masses[name] = M



# test = Material()
# test.add_nuclide('U238', 1)
# test.set_density(1.5, 'g/cm3')

# print(test.get_sf())