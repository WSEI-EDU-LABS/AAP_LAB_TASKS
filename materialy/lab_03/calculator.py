# -*- coding: utf-8 -*-
"""Prosty kalkulator -- klasa demonstracyjna do testowania."""


class Calculator:
    """Prosty kalkulator z czterema podstawowymi operacjami."""

    def add(self, a, b):
        """Zwraca sume dwoch liczb."""
        return a + b

    def subtract(self, a, b):
        """Zwraca roznice dwoch liczb."""
        return a - b

    def multiply(self, a, b):
        """Zwraca iloczyn dwoch liczb."""
        return a * b

    def divide(self, a, b):
        """Zwraca iloraz dwoch liczb. Rzuca ValueError przy dzieleniu przez zero."""
        if b == 0:
            raise ValueError("Dzielenie przez zero!")
        return a / b
