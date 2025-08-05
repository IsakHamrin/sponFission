# nuclide_densities = {
#     'O16': 4.76318709979466E-02,
#     'Th232': 7.06104652673138E-15,
#     'U233': 2.35088603140821E-11,
#     'U234': 3.04159895434244E-08,
#     'U235': 4.49538785711297E-04,
#     'U236': 6.89750759080931E-05,
#     'U238': 2.26704289203308E-02,
#     'Np237': 4.55266877773770E-06,
#     'Pu236': 1.89748994915674E-14,
#     'Pu238': 7.46428645473517E-07,
#     'Pu239': 1.24397804220399E-04,
#     'Pu240': 2.91722130669398E-05,
#     'Pu241': 1.62079695976725E-05,
#     'Pu242': 2.48409460618007E-06,
#     'Am241': 3.48993557415652E-07,
#     'Cm242': 6.91986026960431E-08,
#     'Cm244': 3.34182840687710E-08,
#     'Cm246': 3.15376964764952E-11
# }

# total_density = sum(nuclide_densities.values())
# atom_fractions = {k: v / total_density for k, v in nuclide_densities.items()}
# # print(atom_fractions)
# # print(total_density)

# from material import Material 

# # Initialize the material
# m = Material()
# m.set_density('g/cm3', 10.5)
# m.set_volume(1.0)

# # Add all nuclides with normalized atom fractions
# for name, fraction in nuclide_densities.items():
#     m.add_nuclide(name, fraction)

# # print(m)
# print("Spontaneous fission rate:", m.get_sf(), "fissions/s")

import unittest
import sponFission as sf
# import spontaneousfission as sf  # your package name here

class TestSpontaneousFission(unittest.TestCase):
    def test_serpent_example(self):
        mat = sf.Material()
        mat.set_volume(1.0)
        mat.set_number_densities(True)  # Indicate absolute number densities
        mat.set_density(10.5, 'g/cm3')

        # Add nuclides with atomic densities to get atoms/cm³
        mat.add_nuclide('O16',     4.76318709979466E-02)
        mat.add_nuclide('Th232',   7.06104652673138E-15)
        mat.add_nuclide('U233',    2.35088603140821E-11)
        mat.add_nuclide('U234',    3.04159895434244E-08)
        mat.add_nuclide('U235',    4.49538785711297E-04)
        mat.add_nuclide('U236',    6.89750759080931E-05)
        mat.add_nuclide('U238',    2.26704289203308E-02)
        mat.add_nuclide('Np237',   4.55266877773770E-06)
        mat.add_nuclide('Pu236',   1.89748994915674E-14)
        mat.add_nuclide('Pu238',   7.46428645473517E-07)
        mat.add_nuclide('Pu239',   1.24397804220399E-04)
        mat.add_nuclide('Pu240',   2.91722130669398E-05)
        mat.add_nuclide('Pu241',   1.62079695976725E-05)
        mat.add_nuclide('Pu242',   2.48409460618007E-06)
        mat.add_nuclide('Am241',   3.48993557415652E-07)
        mat.add_nuclide('Cm242',   6.91986026960431E-08)
        mat.add_nuclide('Cm244',   3.34182840687710E-08)
        mat.add_nuclide('Cm246',   3.15376964764952E-11)

        sfr = mat.get_sf()

        # Check that the calculated SFR is close to expected ~277 fissions/s
        self.assertAlmostEqual(sfr, 277.1, delta=5)

if __name__ == '__main__':
    unittest.main()
