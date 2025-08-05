from .data import sf_data, molar_masses

ABSOLUTE = False

def add_nuclide_data(name, half_life, sf_branching_ratio, molar_mass=None):
    """
    Add a new nuclide to the spontaneous fission dataset and optionally to the molar mass dictionary.
    
    Parameters
    ----------
    name : str
        Name of the nuclide (e.g., 'Cs137').
    half_life : float
        Half-life in seconds.
    sf_branching_ratio : float
        Spontaneous fission branching ratio in percent (e.g., 0.01 for 0.01%).
    molar_mass : float, optional
        Molar mass in g/mol (if known).
    """
    sf_data[name] = {
        'half_life': half_life,
        'sf_branching_ratio': sf_branching_ratio
    }
    if molar_mass is not None:
        molar_masses[name] = molar_mass
