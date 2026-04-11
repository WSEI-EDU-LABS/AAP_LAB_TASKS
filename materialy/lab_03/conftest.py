# -*- coding: utf-8 -*-
"""conftest.py -- centralny plik konfiguracyjny pytest.

Fixtures zdefiniowane tutaj sa automatycznie dostepne we WSZYSTKICH
plikach testowych w tym katalogu (i podkatalogach).
Nie trzeba ich importowac -- pytest wykrywa je sam.
"""

import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    """Fixture tworzacy instancje Calculator -- dostepny globalnie."""
    return Calculator()
