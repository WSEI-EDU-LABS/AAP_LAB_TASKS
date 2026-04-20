# -*- coding: utf-8 -*-
"""Testy pytest dla klasy Product -- uzupelnij!

Uruchomienie: pytest test_product_pytest.py -v
"""

import pytest
from product import Product


# --- Fixture ---

@pytest.fixture
def product():
    """Tworzy instancje Product do testow (odpowiednik setUp)."""
    return Product("Laptop", 2999.99, 10)


# --- Testy z fixture ---

def test_is_available(product):
    """Sprawdz dostepnosc produktu."""
    assert product.is_available() is True



def test_total_value(product):
    """Sprawdz wartosc calkowita."""
    oczekiwana_wartosc = product.price * product.quantity
    assert product.total_value() == oczekiwana_wartosc


# --- Testy z parametryzacja ---

@pytest.mark.parametrize("amount, expected_quantity", [
    # TODO: Dodaj przypadki testowe jako krotki, np.:
    (5, 15),   # dodanie 5 do poczatkowych 10 = 15
    (0, 10),   # dodanie 0 = bez zmian
    (100, 110),  # dodanie 100
])
def test_add_stock_parametrized(product, amount, expected_quantity):
    """Testuje add_stock z roznymi wartosciami."""
    # TODO: Wywolaj product.add_stock(amount) i sprawdz product.quantity
    product.add_stock(amount)
    assert product.quantity == expected_quantity


# --- Testy bledow ---

def test_remove_stock_too_much_raises(product):
    """Sprawdz, czy proba usuniecia za duzej ilosci rzuca ValueError."""
    # TODO: Uzyj with pytest.raises(ValueError):
    with pytest.raises(ValueError):
        product.remove_stock(20)


def test_add_stock_negative_raises(product):
    """Sprawdz, czy ujemna wartosc w add_stock rzuca ValueError."""
    # TODO: Uzyj with pytest.raises(ValueError):
    with pytest.raises(ValueError):
        product.add_stock(-5)
