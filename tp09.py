import unittest
from tp07 import Fraction

class TestFraction(unittest.TestCase):

    def test_init(self):
        self.assertEqual(str(Fraction(1, 2)), "1/2")
        self.assertEqual(str(Fraction(-3, 6)), "-1/2")
        self.assertEqual(str(Fraction(4, -8)), "-1/2")
        self.assertEqual(str(Fraction(0, 5)), "0")
        with self.assertRaises(ValueError):
            Fraction(1, 0)
        self.assertEqual(str(Fraction(5, 1)), "5")

    def test_add(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertEqual(str(f1 + f2), "5/6")
        self.assertEqual(str(Fraction(1, 2) + Fraction(-1, 2)), "0")
        f3 = Fraction(1, 4)
        self.assertEqual(str(f1 + f3), "3/4")

    def test_sub(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        self.assertEqual(str(f1 - f2), "1/6")
        self.assertEqual(str(f1 - f1), "0")
        f3 = Fraction(-1, 2)
        self.assertEqual(str(f1 - f3), "1")

    def test_mul(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        self.assertEqual(str(f1 * f2), "1/3")
        f3 = Fraction(0, 5)
        self.assertEqual(str(f1 * f3), "0")

    def test_truediv(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        self.assertEqual(str(f1 / f2), "3/4")
        with self.assertRaises(ZeroDivisionError):
            f1 / Fraction(0, 1)
        f3 = Fraction(1, 1)
        self.assertEqual(str(f1 / f3), "1/2")

    def test_pow(self):
        f1 = Fraction(2, 3)
        self.assertEqual(str(f1 ** 2), "4/9")
        self.assertEqual(str(f1 ** -1), "3/2")
        self.assertEqual(str(f1 ** 0), "1")

    def test_float_conversion(self):
        f1 = Fraction(1, 2)
        self.assertAlmostEqual(float(f1), 0.5)
        f2 = Fraction(4, 2)
        self.assertEqual(float(f2), 2.0)



    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            Fraction(1.5, 2)
        with self.assertRaises(TypeError):
            Fraction(True, 2)
        with self.assertRaises(TypeError):
            Fraction(1, False)

    def test_comparison(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 4)
        f3 = Fraction(1, 3)
        self.assertTrue(f1 == f2)
        self.assertTrue(f1 > f3)
        self.assertFalse(f1 <= f3)
        self.assertTrue(f1 < Fraction(3, 2))
        self.assertTrue(f1 >= f2)
        self.assertTrue(f1 >= f3)

    def test_as_mixed_number(self):
        f1 = Fraction(5, 2)
        self.assertEqual(f1.as_mixed_number(), "2 and 1/2")
        f2 = Fraction(7, 3)
        self.assertEqual(f2.as_mixed_number(), "2 and 1/3")
        f3 = Fraction(3, 1)
        self.assertEqual(f3.as_mixed_number(), "3")

    def test_edge_cases(self):
        f1 = Fraction(1000000, 2000000)
        self.assertEqual(str(f1), "1/2")
        f2 = Fraction(-1, 3)
        self.assertEqual(str(f2), "-1/3")
        f3 = Fraction(1, 1000000)
        self.assertEqual(str(f3), "1/1000000")
        f4 = Fraction(-7, 4)
        self.assertEqual(str(f4), "-7/4")


    def test_simplify(self):
        f1 = Fraction(6, 8)
        self.assertEqual(str(f1), "3/4")
        f2 = Fraction(9, 3)
        self.assertEqual(str(f2), "3")

    def test_as_decimal(self):
        f1 = Fraction(5, 4)
        self.assertAlmostEqual(f1.as_decimal(), 1.25)
        f2 = Fraction(1, 3)
        self.assertAlmostEqual(f2.as_decimal(), 0.3333, places=4)

    def test_addition_with_integer(self):
        f1 = Fraction(1, 2)
        self.assertEqual(str(f1 + 1), "3/2")
        f2 = Fraction(3, 5)
        self.assertEqual(str(f2 + 2), "13/5")

        def test_division_with_integer(self):
            # Test division avec un entier
            f1 = Fraction(5, 4)
            self.assertEqual(str(f1 / 2), "5/8")  # 5/4 / 2 = 5/8

            f2 = Fraction(7, 3)
            self.assertEqual(str(f2 / 3), "7/9")  # 7/3 / 3 = 7/9

        def test_fraction_equality(self):
            # Test d'égalité des fractions
            f1 = Fraction(4, 6)
            f2 = Fraction(2, 3)
            self.assertTrue(f1 == f2)  # Les deux fractions sont égales après simplification

            f3 = Fraction(1, 2)
            f4 = Fraction(1, 3)
            self.assertFalse(f3 == f4)  # Fractions différentes

        def test_negative_fractions(self):
            # Test fractions négatives
            f1 = Fraction(-1, 2)
            self.assertEqual(str(f1), "-1/2")

            f2 = Fraction(1, -2)
            self.assertEqual(str(f2), "-1/2")

            f3 = Fraction(-3, -4)
            self.assertEqual(str(f3), "3/4")

        def test_fraction_as_string(self):
            # Test de la conversion en chaîne de caractères
            f1 = Fraction(7, 9)
            self.assertEqual(str(f1), "7/9")

            f2 = Fraction(3, 5)
            self.assertEqual(str(f2), "3/5")

    if __name__ == "__main__":
        unittest.main()
