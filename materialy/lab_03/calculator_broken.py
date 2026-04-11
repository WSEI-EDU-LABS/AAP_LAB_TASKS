# -*- coding: utf-8 -*-
"""
ZEPSUTY Calculator do DEMO RED na slajdzie 13.

UWAGA: Ten plik celowo zawiera bug w metodzie `add` (zwraca a+b+1 zamiast a+b)
oraz w `multiply` (zwraca a*b+1 zamiast a*b). Sluzy WYLACZNIE do demonstracji,
jak wyglada output testow, ktore PADAJA.

Dzieki temu instruktor moze pokazac:
1. Jak wyglada czerwony output unittest
2. Jak czytac traceback i AssertionError
3. Dlaczego zielony output to nie wszystko — czerwony to 80% pracy z testami

NIE EDYTUJ TEGO PLIKU. Aby zobaczyc dzialanie, uruchom:
    python -m unittest test_calculator_broken_demo -v
"""


class Calculator:
    """Calculator z celowymi bugami — TYLKO do demonstracji RED output."""

    def add(self, a, b):
        """BUG: dodaje 1 do wyniku (off-by-one error)."""
        return a + b + 1  # <-- celowy bug

    def subtract(self, a, b):
        """Ta metoda dziala poprawnie."""
        return a - b

    def multiply(self, a, b):
        """BUG: dodaje 1 do wyniku."""
        return a * b + 1  # <-- celowy bug

    def divide(self, a, b):
        """Ta metoda dziala poprawnie."""
        if b == 0:
            raise ValueError("Dzielenie przez zero!")
        return a / b
