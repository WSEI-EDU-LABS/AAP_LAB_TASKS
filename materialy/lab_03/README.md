# 🧪 Lab 03 — Testowanie w Pythonie: `unittest` i `pytest`

> **Kurs:** Automatyzacja i Analiza Procesów (AAP) · WSEI  
> **Temat:** Pisanie i uruchamianie testów jednostkowych w Pythonie

---

## 📁 Struktura plików

```
lab_03/
│
├── README.md                        ← ten plik
├── pytest.ini                       ← konfiguracja pytest (działa automatycznie)
├── conftest.py                      ← globalne fixtures dostępne dla wszystkich testów
│
├── calculator.py                    ← klasa Calculator (gotowa, do demonstracji)
├── calculator_broken.py             ← klasa z celowymi błędami (ćwiczenie debugowania)
├── product.py                       ← klasa Product (do samodzielnej implementacji ⚠️)
│
├── test_calculator_pytest.py        ← testy pytest dla Calculator
├── test_calculator_unittest.py      ← testy unittest dla Calculator
├── test_calculator_broken_demo.py   ← demonstracja wykrywania błędów
├── test_product_pytest.py           ← testy pytest dla Product (do uzupełnienia ✏️)
└── test_product_unittest.py         ← testy unittest dla Product (do uzupełnienia ✏️)
```

---

## ⚙️ Wymagania

Przed uruchomieniem testów upewnij się, że masz zainstalowany `pytest`:

```bash
pip install pytest
```

Sprawdź wersję:

```bash
pytest --version
```

---

## 🚀 Uruchamianie testów — komendy

### 1. Przejdź do katalogu z laboratorium

```bash
cd "/Users/macbook/Desktop/WSEI EDU/AAP_LAB_TASKS/materialy/lab_03"
```

---

### 2. Uruchom WSZYSTKIE testy naraz

```bash
pytest
```

> pytest automatycznie znajdzie wszystkie pliki `test_*.py` w katalogu  
> (skonfigurowane w `pytest.ini`)

---

### 3. Uruchom konkretny plik testowy

```bash
# Testy dla Product (pytest)
pytest test_product_pytest.py

# Testy dla Calculator (pytest)
pytest test_calculator_pytest.py

# Testy dla Calculator (unittest syntax, ale uruchamiane przez pytest)
pytest test_calculator_unittest.py
```

---

### 4. Uruchom jeden konkretny test

```bash
# Składnia: pytest PLIK::NAZWA_TESTU
pytest test_product_pytest.py::test_is_available
pytest test_calculator_pytest.py::test_add
```

---

### 5. Uruchom testy z konkretnym markerem (np. parametryzowane)

```bash
pytest -k "parametrized"
pytest -k "add or subtract"
```

---

## 🔍 Wyjaśnienie flag i opcji

| Flaga / opcja | Co robi |
|---|---|
| `-v` | **verbose** — pokazuje każdy test osobno z nazwą i wynikiem (`PASSED` / `FAILED`) |
| `-s` | **no capture** — pokazuje `print()` i inne wyjście standardowe w trakcie testów |
| `-x` | **exitfirst** — zatrzymuje się po **pierwszym** nieudanym teście |
| `--tb=short` | **traceback short** — skrócony opis błędu (dobry na co dzień) |
| `--tb=long` | **traceback long** — pełny opis błędu z całym traceback |
| `--tb=no` | wyłącza wyświetlanie szczegółów błędów |
| `-k "wyraz"` | uruchamia tylko testy, których **nazwa zawiera** podany wyraz |
| `--co` | **collect-only** — tylko wylistuje testy, bez ich uruchamiania |
| `-q` | **quiet** — minimalne wyjście, tylko podsumowanie |

### Przykłady z flagami:

```bash
# Szczegółowy tryb + pełne błędy
pytest test_product_pytest.py -v --tb=long

# Tylko lista testów (bez uruchamiania)
pytest --co

# Zatrzymaj po pierwszym błędzie, pokaż print()
pytest -x -s

# Cichy tryb — tylko podsumowanie
pytest -q
```

---

## 📐 Jak działa `pytest.ini`

Plik `pytest.ini` w tym katalogu automatycznie ustawia domyślne opcje:

```ini
[pytest]
addopts = -v --tb=short   ← każde uruchomienie pytest ma -v i --tb=short z automatu
testpaths = .             ← szuka testów w bieżącym katalogu
python_files = test_*.py  ← pliki testowe muszą zaczynać się od "test_"
```

Dzięki temu **nie musisz** za każdym razem wpisywać `-v` — jest już domyślnie włączone.

---

## 🔧 Jak działa `conftest.py`

Plik `conftest.py` definiuje **globalne fixtures** dostępne we wszystkich plikach testowych:

```python
@pytest.fixture
def calc():
    return Calculator()   # ← gotowa instancja dla każdego testu
```

Fixture z `conftest.py` możesz użyć w **dowolnym** pliku testowym **bez importowania** — pytest wykrywa je automatycznie.

---

## 🧩 Kluczowe pojęcia

### Fixture (`@pytest.fixture`)
Funkcja przygotowująca dane lub obiekt przed testem — odpowiednik `setUp()` z `unittest`.

```python
@pytest.fixture
def product():
    return Product("Laptop", 2999.99, 10)   # ← gotowy obiekt do testów

def test_is_available(product):             # ← pytest wstrzykuje fixture automatycznie
    assert product.is_available() == True
```

---

### Parametryzacja (`@pytest.mark.parametrize`)
Uruchamia ten sam test wielokrotnie z różnymi danymi wejściowymi.

```python
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected
```

> Zamiast pisać 3 osobne testy — piszesz jeden z tabelką danych wejściowych.

---

### Testowanie wyjątków (`pytest.raises`)
Sprawdza, czy funkcja rzuca oczekiwany wyjątek.

```python
def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(10, 0)
```

---

## ✏️ Twoje zadanie

Pliki do uzupełnienia:

1. **`product.py`** — zaimplementuj klasę `Product` (konstruktor + 4 metody)
2. **`test_product_pytest.py`** — uzupełnij fixture i testy (szukaj `# TODO`)
3. **`test_product_unittest.py`** — uzupełnij odpowiedniki w stylu unittest

### Kolejność pracy:
```
1. Zaimplementuj product.py
2. Uruchom: pytest test_product_pytest.py  → zobaczysz błędy
3. Uzupełniaj testy po kolei
4. Uruchom ponownie → aż wszystkie są PASSED ✅
```

---

## 📊 Interpretacja wyników

```
PASSED   ✅  — test przeszedł, kod działa poprawnie
FAILED   ❌  — test nie przeszedł, znaleziono błąd
ERROR    💥  — błąd w samym teście lub fixture (np. brak importu)
SKIPPED  ⏭️  — test pominięty (np. oznaczony @pytest.mark.skip)
```

### Przykład dobrego wyniku:
```
test_calculator_pytest.py::test_add          PASSED
test_calculator_pytest.py::test_subtract     PASSED
test_calculator_pytest.py::test_divide_zero  PASSED

===================== 3 passed in 0.12s =====================
```

---

*Laboratorium 3 · AAP · WSEI · 2026*
