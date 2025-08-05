import unittest
import sponFission as sf

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
