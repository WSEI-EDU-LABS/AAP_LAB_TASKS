# Zestaw zaliczeniowy — Architektura Aplikacji w Pythonie

**Termin oddania:** 27.06.2026r.
**Forma:** wypełniony Jupyter Notebook + krótkie sprawozdanie w pliku Markdown.

---

## Co znajduje się w folderze

| Plik | Opis |
|------|------|
| `AAP_Zestaw_Zaliczeniowy.ipynb` | Główny notebook — 6 labów × (teoria + przykład + zadanie) |
| `preflight_download.py` | **Uruchom RAZ przed otwarciem notebooka** — sprawdza pakiety i pobiera dataset |
| `README.md` | Ten plik |

---

## Jak zacząć (3 kroki)

```bash
# 1. Aktywuj venv z laboratorium 5 (PySpark)
source ../venv/bin/activate

# 2. Doinstaluj pakiety potrzebne tylko temu zestawowi
pip install datasets scikit-learn jupyter

# 3. Pobierz dataset i sprawdz srodowisko (RAZ, ~30s)
python preflight_download.py

# 4. Otworz notebook
jupyter notebook AAP_Zestaw_Zaliczeniowy.ipynb
```

`preflight_download.py` pobiera dataset **`stanfordnlp/imdb`** (50 000 recenzji, ~80 MB) z Hugging Face Hub i zapisuje go w cache (`~/.cache/huggingface/`). Wszystkie kolejne wywołania `load_dataset()` w notebooku są **instant** dzięki temu cache.

---

## Dane źródłowe — co używasz

| Lab | Dataset | Skąd | Rozmiar |
|-----|---------|------|---------|
| 1-6 | `stanfordnlp/imdb` | [Hugging Face](https://huggingface.co/datasets/stanfordnlp/imdb) | 80 MB (zcache'owany) |

**Ważne:** dataset jest na HF zsortowany po labelu (najpierw 12500 negatywnych, potem 12500 pozytywnych). Notebook ma w `get_imdb_subset()` `.shuffle(seed=42)` — bez tego dostawałbyś 100% jednej klasy.

---

## Struktura każdej sekcji

Każdy z 6 labów ma identyczną strukturę:

1. **Teoria w trzech zdaniach** — esencja konceptu, do której zawsze możesz wrócić.
2. **Przykład rozwiązany** — gotowy działający kod ilustrujący koncept.
3. **Twoje zadanie** — analogiczne ćwiczenie z rozszerzonym zakresem (komórka z `# TODO`).

Wystarczy wypełnić komórki z `# TODO` i odesłać notebook.

---

## Ocenianie

| Waga | Kryterium |
|------|-----------|
| 50% | Poprawność (czy działa, czy spełnia specyfikację) |
| 30% | Jakość kodu (czytelność, typowanie, brak duplikacji) |
| 20% | Insight — refleksja o tym, dlaczego coś działa lub nie działa |

---

## FAQ

**Q: Czy mogę użyć innego datasetu niż imdb?**
A: Tak, jeśli ma podobny rozmiar (10k+ próbek tekstowych z etykietą). Uzasadnij wybór.

**Q: Czy mogę pominąć jedno zadanie?**
A: Tak, ale wtedy maksymalna ocena to 5/6 zadań × 100% = 83%.

**Q: Czy PySpark musi działać lokalnie?**
A: Tak. Setup w notebooku automatycznie wykrywa JAVA_HOME na macOS/Linux. Jeśli masz problem — skonfiguruj zmienne `JAVA_HOME` i `PYSPARK_PYTHON` ręcznie zgodnie z dokumentacją Spark.

**Q: Co jeśli HF Hub nie działa / brak internetu?**
A: Po pierwszym `preflight_download.py` dataset jest **lokalnie w `~/.cache/huggingface/`**. Możesz pracować całkowicie offline.

**Q: Czy mogę użyć ChatGPT/Copilot/Claude?**
A: Tak, ale **musisz rozumieć każdą linijkę** którą oddajesz. Na zaliczeniu ustnym poproszę o wyjaśnienie wybranego fragmentu.
