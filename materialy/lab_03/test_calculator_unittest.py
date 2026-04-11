# -*- coding: utf-8 -*-
"""Testy jednostkowe klasy Calculator z uzyciem modulu unittest."""

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Klasa testowa dla Calculator -- dziedziczy po unittest.TestCase."""

    def setUp(self):
        """Tworzy nowa instancje Calculator przed KAZDYM testem."""
        self.calc = Calculator()

    def tearDown(self):
        """Sprzatanie po kazdym tescie (tutaj niepotrzebne, ale pokazujemy koncepcje)."""
        pass

    # --- Testy metody add ---

    def test_add_positive_numbers(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        result = self.calc.add(-1, -1)
        self.assertEqual(result, -2)

    def test_add_mixed_numbers(self):
        result = self.calc.add(-1, 1)
        self.assertEqual(result, 0)

    # --- Testy metody subtract ---

    def test_subtract(self):
        result = self.calc.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_subtract_negative_result(self):
        result = self.calc.subtract(5, 10)
        self.assertEqual(result, -5)

    # --- Testy metody multiply ---

    def test_multiply(self):
        result = self.calc.multiply(3, 7)
        self.assertEqual(result, 21)

    def test_multiply_by_zero(self):
        result = self.calc.multiply(100, 0)
        self.assertEqual(result, 0)

    # --- Testy metody divide ---

    def test_divide(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5.0)

    def test_divide_returns_float(self):
        result = self.calc.divide(7, 2)
        self.assertEqual(result, 3.5)

    def test_divide_by_zero_raises_error(self):
        """Sprawdza, czy dzielenie przez zero rzuca ValueError."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
