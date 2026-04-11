# -*- coding: utf-8 -*-
"""
Testy DEMO RED — uzywaja zepsutego Calculator-a do demonstracji,
jak wyglada output gdy testy padaja.

Te testy sa IDENTYCZNE jak w test_calculator_unittest.py,
ale importuja Calculator z calculator_broken.py zamiast calculator.py.

Uruchom:
    python -m unittest test_calculator_broken_demo -v

Spodziewany rezultat:
    - 5 testow PASSED (subtract, divide, divide_by_zero)
    - 5 testow FAILED (wszystkie add* i multiply*)
    - Output zawiera tracebacki z AssertionError
"""

import unittest
from calculator_broken import Calculator


class TestCalculator(unittest.TestCase):
    """Klasa testowa identyczna jak normalna — ale Calculator jest zepsuty."""

    def setUp(self):
        self.calc = Calculator()

    def tearDown(self):
        pass

    # --- Testy metody add (BEDA PADAC — bug: a+b+1) ---

    def test_add_positive_numbers(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)  # FAIL: 6 != 5

    def test_add_negative_numbers(self):
        result = self.calc.add(-1, -1)
        self.assertEqual(result, -2)  # FAIL: -1 != -2

    def test_add_mixed_numbers(self):
        result = self.calc.add(-1, 1)
        self.assertEqual(result, 0)  # FAIL: 1 != 0

    # --- Testy metody subtract (POWINNY PRZEJSC) ---

    def test_subtract(self):
        result = self.calc.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_subtract_negative_result(self):
        result = self.calc.subtract(5, 10)
        self.assertEqual(result, -5)

    # --- Testy metody multiply (BEDA PADAC — bug: a*b+1) ---

    def test_multiply(self):
        result = self.calc.multiply(3, 7)
        self.assertEqual(result, 21)  # FAIL: 22 != 21

    def test_multiply_by_zero(self):
        result = self.calc.multiply(100, 0)
        self.assertEqual(result, 0)  # FAIL: 1 != 0

    # --- Testy metody divide (POWINNY PRZEJSC) ---

    def test_divide(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5.0)

    def test_divide_returns_float(self):
        result = self.calc.divide(7, 2)
        self.assertEqual(result, 3.5)

    def test_divide_by_zero_raises_error(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
