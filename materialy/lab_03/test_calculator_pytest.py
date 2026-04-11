# -*- coding: utf-8 -*-
"""Testy klasy Calculator z uzyciem pytest -- porownaj z wersja unittest!"""

import pytest
from calculator import Calculator


# --- Fixture zastepuje setUp z unittest ---

@pytest.fixture
def calc():
    """Tworzy instancje Calculator -- odpowiednik setUp w unittest."""
    return Calculator()


# --- Podstawowe testy (proste funkcje, nie klasa!) ---

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0


def test_subtract(calc):
    assert calc.subtract(10, 5) == 5
    assert calc.subtract(5, 10) == -5


def test_multiply(calc):
    assert calc.multiply(3, 7) == 21
    assert calc.multiply(100, 0) == 0


def test_divide(calc):
    assert calc.divide(10, 2) == 5.0
    assert calc.divide(7, 2) == 3.5


def test_divide_by_zero(calc):
    """pytest.raises to odpowiednik assertRaises z unittest."""
    with pytest.raises(ValueError):
        calc.divide(10, 0)


# --- Parametryzacja -- jeden test, wiele zestawow danych ---

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (100, -50, 50),
    (-10, -20, -30),
])
def test_add_parametrized(a, b, expected):
    calc = Calculator()
    assert calc.add(a, b) == expected


# --- Marks -- oznaczanie testow ---

@pytest.mark.skip(reason="Przyklad: ten test jest celowo pomijany")
def test_skipped_example():
    """Ten test nie zostanie uruchomiony -- sluzy jako przyklad @pytest.mark.skip."""
    assert False


@pytest.mark.xfail(reason="Przyklad: oczekujemy niepowodzenia tego testu")
def test_xfail_example():
    """Ten test ma prawo nie przejsc -- sluzy jako przyklad @pytest.mark.xfail."""
    calc = Calculator()
    assert calc.add(1, 1) == 3  # celowo bledne oczekiwanie
