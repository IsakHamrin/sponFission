from data import sf_data
from data import molar_masses
import numpy as np


AVOGADRO = 6.02214076e23

class Material:
    def __init__(self):
        self.nuclides = []
        self.atomic_fractions = []
        self.density = 0
        self.unit = ''
        self.volume = None
    
    def __str__(self):
        name = ''
        for n in self.nuclides:
            name += n + ' '
        if self.volume == None:
            return f'Nuclide: {name}, {self.density} {self.unit}'
        else:
            return f'Nuclide: {name}, {self.density} {self.unit}, {self.volume}'

    def add_nuclide(self, name:str, atomic_fraction:float):
        self.nuclides.append(name)
        self.atomic_fractions.append(atomic_fraction)

    def set_density(self, unit:str, density:float):
        self.unit = unit
        self.density = density
    
    def set_volume(self, volume:float):
        self.volume = volume

    def get_sf(self):
        # for i, nuclide in enumerate(self.nuclides):
        #     if nuclide not in sf_data:
        #         print(f"Warning: No data for {nuclide}, removing.")
        #         delete = i
        #         # continue
        # self.nuclides.pop(delete)
        # self.atomic_fractions.pop(delete)
        total_fraction = sum(self.atomic_fractions)
        # frac=0
        sf_tot = 0
        for i, nuclide in enumerate(self.nuclides):
            if nuclide not in sf_data:
                print(f"Warning: No data for {nuclide}, skipping.")
                # sf += 0
                continue

            half_life = sf_data[nuclide]['half_life']#*365.25*24*3600 #To get in seconds
            # print(f'halflife: {half_life}')
            Pi = sf_data[nuclide]['sf_branching_ratio'] * 0.01
            # frac = self.atomic_fractions[i] / total_fraction
            # print(frac)

            Lambda = np.log(2) / half_life

            number_density = self.atomic_fractions[i] * 1e24
            print(number_density)

            molar_mass = molar_masses[nuclide]
            # number_density = (self.density / molar_mass) * AVOGADRO * frac  # atoms/cm³

            sf = number_density * Lambda * Pi
            sf_tot += sf
            print(f'{nuclide}: {sf}')
        if self.volume == None:
            return sf_tot  # fissions/s/cm³
        else:
            return sf_tot * self.volume  # fissions/s



