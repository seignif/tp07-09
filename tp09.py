import unittest
from tp07 import Fraction

class TestFraction(unittest.TestCase):

    def test_init(self):
        # Test initialisation normale
        self.assertEqual(str(Fraction(1, 2)), "1/2")
        self.assertEqual(str(Fraction(-3, 6)), "-1/2")  # Simplification
        self.assertEqual(str(Fraction(4, -8)), "-1/2")
        self.assertEqual(str(Fraction(0, 5)), "0")

        # Test dénominateur zéro
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_add(self):
        # Test addition
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertEqual(str(f1 + f2), "5/6")
        self.assertEqual(str(Fraction(1, 2) + Fraction(-1, 2)), "0")

    def test_sub(self):
        # Test soustraction
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertEqual(str(f1 - f2), "1/6")
        self.assertEqual(str(f1 - f1), "0")

    def test_mul(self):
        # Test multiplication
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        self.assertEqual(str(f1 * f2), "1/3")

    def test_truediv(self):
        # Test division
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        self.assertEqual(str(f1 / f2), "3/4")

        # Test division par une fraction nulle
        with self.assertRaises(ZeroDivisionError):
            f1 / Fraction(0, 1)

    def test_pow(self):
        # Test puissance
        f1 = Fraction(2, 3)
        self.assertEqual(str(f1 ** 2), "4/9")
        self.assertEqual(str(f1 ** -1), "3/2")  # Inverse

    def test_float_conversion(self):
        # Test conversion en float
        f1 = Fraction(1, 2)
        self.assertAlmostEqual(float(f1), 0.5)

    def test_properties(self):
        # Test des propriétés
        self.assertTrue(Fraction(0, 1).is_zero())
        self.assertTrue(Fraction(4, 2).is_integer())
        self.assertTrue(Fraction(1, 2).is_proper())
        self.assertTrue(Fraction(1, 3).is_unit())
        self.assertTrue(Fraction(1, 2).is_adjacent_to(Fraction(1, 3)))

    def test_invalid_inputs(self):
        # Test initialisation avec des valeurs non entières
        with self.assertRaises(TypeError):
            Fraction(1.5, 2)

        with self.assertRaises(TypeError):
            Fraction(True, 2)

        with self.assertRaises(TypeError):
            Fraction(1, False)

if __name__ == "__main__":
    unittest.main()



