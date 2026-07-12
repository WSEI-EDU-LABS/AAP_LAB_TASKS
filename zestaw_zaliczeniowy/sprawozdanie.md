# Sprawozdanie z Laboratoriów (1.1 – 6.1)

## Lab 1 — Dekoratory i stabilność API (Zadanie 1.1)

- **Cel:** Implementacja produkcyjnej jakości dekoratorów `@retry` (z wykładniczym backoffem) oraz `@cache_to_disk` (zapis wyników do JSON na bazie hasha MD5).
- **Weryfikacja:** Testy na niestabilnej funkcji `flaky_fetch` (50% szans na błąd).
- **Insight do raportu:** \* Teoretyczna szansa sukcesu dla `max_attempts=5` wynosi:
  $$P(\text{sukces}) = 1 - 0.5^5 = 1 - 0.03125 = 0.96875 \text{ (96.9\%)}$$
  - Eksperyment empiryczny na 100 wywołaniach potwierdza teorię – współczynnik sukcesu oscyluje wokół **95% – 98%**.
  - **Wniosek:** Nałożenie `@cache_to_disk` nad `@retry` całkowicie eliminuje ponowne odpytywanie API dla tych samych argumentów, drastycznie podnosząc wydajność i odporność systemu.

---

## Lab 2 — Współbieżność i równoległość (Zadanie 2.1)

- **Cel:** Równoległe obliczanie uproszczonego score sentymentu (lexicon-based) dla 5000 recenzji IMDb.
- **Wyniki pomiarów:**
  - _Sekwencyjnie:_ Najwolniejszy czas wykonania.
  - _ThreadPool:_ Brak zauważalnego przyspieszenia w stosunku do wersji sekwencyjnej.
  - _Multiprocessing:_ Wyraźny zwycięzca (wielokrotne przyspieszenie proporcjonalne do liczby rdzeni).
- **Odpowiedź na pytanie:** Wariant **Multiprocessing jest najszybszy**. Analiza tekstu (tokenizacja regex, zliczanie słów) to zadanie czysto obliczeniowe (**CPU-bound**). W Pythonie mechanizm GIL blokuje jednoczesne wykonywanie kodu bajtowego przez wiele wątków, przez co `ThreadPool` nie daje zysku. `Multiprocessing` tworzy osobne procesy z własnymi interpreterami, skutecznie omijając GIL i wykorzystując pełną moc procesora wielordzeniowego.
  - _Uwaga techniczna:_ Na systemach macOS w środowisku Jupyter Notebook wymagane jest przeniesienie funkcji do zewnętrznego pliku `.py` (metoda startowa `spawn`) lub wymuszenie kontekstu `fork`.

---

## Lab 3 — Testowanie z pytest (Zadanie 3.1)

- **Cel:** Implementacja klasy `Tokenizer` (czyszczenie HTML, lowercase, obsługa standardu Unicode) oraz zestawu testów w `pytest` z użyciem asercji akceptacji, fixtur, parametryzacji i flagi `xfail`.
- **Insight do raportu (Heurystyka rozmiaru słownika):**
  - Przetwarzanie 20 losowych recenzji generuje unikalny słownik na poziomie ok. **1300 – 1600** tokenów.
  - Dla **100 recenzji** przewidywany rozmiar słownika wynosi ok. **3200 – 3800** unikalnych słów.
  - **Wniosek:** Przyrost słownika nie jest liniowy, co wynika z **Prawa Heapa** ($V_R = K \cdot N^\beta$). Kolejne teksty w dużym stopniu powielają popularne słowa, przez co tempo przyrostu nowych unikalnych tokenów gwałtownie spada.

---

## Lab 4 — Bazy danych (Zadanie 4.1)

- **Cel:** Projekt alternatywnego schematu bazodanowego NoSQL-style (kolumna tekstowa JSON) w SQLite i wykonanie agregacji za pomocą `json_extract`.
- **Odpowiedź na pytanie (Wniosek):**
  Dla tego problemu **lepszy jest klasyczny schemat relacyjny (SQL)** z dwóch powodów:
  1.  **Rozmiar bazy:** Schemat JSON drastycznie zwiększa narzut pamięciowy przez ciągłe powtarzanie tych samych kluczy (`"text"`, `"label"`, `"stats"`) w każdym wierszu. W SQL schemat definiowany jest tylko raz w metadanych.
  2.  **Czas odczytu i analityki:** Wykonywanie operacji `AVG`, `LIKE` czy `ORDER BY` w strukturze JSON zmusza silnik bazy do parsowania tekstu w locie dla każdego rekordu. Klasyczny SQL operuje na natywnych typach binarnych, co pozwala na pełną optymalizację i indeksowanie pól.

---

## Lab 5 — PySpark Window Functions (Zadanie 5.1)

- **Cel:** Wykorzystanie zaawansowanej analityki okienkowej do rankingu recenzji, wyznaczenia Top 3 per klasa, odchylenia od średniej oraz obliczenia kroczącej średniej.
- **Kluczowe mechanizmy:**
  - `Window.partitionBy("label").orderBy(F.col("word_count").desc())` do precyzyjnego pozycjonowania danych wewnątrz podgrup.
  - Wyznaczenie kroczącej średniej (moving average) z ostatnich 50 recenzji za pomocą ramki okna `.rowsBetween(-49, 0)`.
  - Wizualizacja liniowa w `matplotlib` pozwala na natychmiastowe zaobserwowanie trendów stabilizowania się długości wypowiedzi w miarę napływu danych.

---

## Lab 6 — Data Quality (Zadanie 6.1)

- **Cel:** Budowa autorskiego _Data Quality Framework_ (klasy `DataContract`, `Rule`, `DataValidator`) w oparciu o bibliotekę pandas.
- **Mechanika kontraktu:** \* Rygorystyczne podejście do krytycznych reguł biznesowych o ważności **`severity="error"`** (`no_nulls`, `labels_in_set`, `min/max word_count`) – ich naruszenie skutkuje natychmiastowym przerwaniem procesu (`ValueError`, fail-fast).
  - Reguły o ważności **`severity="warning"`** (`no_duplicates`, `class_balance`, `no_html_tags`) nie blokują pipeline'u, lecz są odnotowywane w raporcie.
  - **Zapis:** Końcowy rezultat walidacji wraz ze szczegółami i sygnaturą czasową (timestamp) jest pomyślnie eksportowany do ustrukturyzowanego pliku `_workspace/data_quality_report.json`.
