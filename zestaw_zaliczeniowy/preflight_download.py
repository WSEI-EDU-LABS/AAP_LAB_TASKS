#!/usr/bin/env python3
"""
Preflight check & download — uruchom RAZ przed otwarciem notebooka.

Zapewnia że wszystkie potrzebne datasety z Hugging Face Hub są pobrane
i zacache'owane lokalnie w ~/.cache/huggingface/.

Użycie:
    python preflight_download.py

Co robi:
1. Sprawdza wymagane pakiety Pythona
2. Pobiera dataset stanfordnlp/imdb (50k recenzji, ~80MB)
3. Wstępnie ładuje go w cache, robi sanity check

Powinien zająć ~30 sekund przy pierwszym uruchomieniu,
< 5 sekund przy kolejnych (dataset już w cache).
"""
import os, sys, time

os.environ["HF_DATASETS_DISABLE_PROGRESS_BAR"] = "1"

REQUIRED_PACKAGES = {
    "datasets": "datasets",
    "pandas": "pandas",
    "pyspark": "pyspark",
    "matplotlib": "matplotlib",
    "sklearn": "scikit-learn",
}


def check_packages():
    print("=== 1/3 Sprawdzanie pakietow ===")
    missing = []
    for module, pip_name in REQUIRED_PACKAGES.items():
        try:
            __import__(module)
            print(f"  [OK]   {module}")
        except ImportError:
            print(f"  [FAIL] {module} -- zainstaluj: pip install {pip_name}")
            missing.append(pip_name)
    if missing:
        print(f"\nBrakuje {len(missing)} pakietow. Zainstaluj:")
        print(f"  pip install {' '.join(missing)}")
        sys.exit(1)


def download_imdb():
    print("\n=== 2/3 Pobieranie datasetu imdb (HF Hub) ===")
    from datasets import load_dataset
    t0 = time.time()
    ds = load_dataset("stanfordnlp/imdb")
    elapsed = time.time() - t0
    n_train = len(ds["train"])
    n_test = len(ds["test"])
    print(f"  Pobranie/cache hit: {elapsed:.1f}s")
    print(f"  Train: {n_train} probek, Test: {n_test} probek")
    return ds


def sanity_check(ds):
    print("\n=== 3/3 Sanity check ===")
    import numpy as np
    # UWAGA: imdb jest sortowany po labelu -> sprawdz mix po shuffle
    sample = ds["train"].shuffle(seed=42).select(range(200))
    labels = [r["label"] for r in sample]
    pos = sum(labels)
    neg = len(labels) - pos
    print(f"  Test shuffle: {pos} pozytywnych / {neg} negatywnych z 200")
    if abs(pos - neg) > 50:
        print("  UWAGA: rozklad nie jest 50/50, ale to OK przy malej probce")
    avg_len = np.mean([len(r["text"].split()) for r in sample])
    print(f"  Srednia dlugosc recenzji: {avg_len:.0f} slow")


if __name__ == "__main__":
    print("=" * 60)
    print("Preflight check — AAP zestaw zaliczeniowy")
    print("=" * 60)
    check_packages()
    ds = download_imdb()
    sanity_check(ds)
    print("\n" + "=" * 60)
    print("OK — mozesz otworzyc AAP_Zestaw_Zaliczeniowy.ipynb")
    print("=" * 60)
