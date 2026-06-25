
import pytest
from tokenizer import Tokenizer

@pytest.fixture
def tokenizer():
    return Tokenizer()

@pytest.fixture
def imdb_sample():
    from datasets import load_dataset
    ds = load_dataset("stanfordnlp/imdb", split="train").shuffle(seed=42).select(range(20))
    return [r["text"] for r in ds]

@pytest.mark.parametrize("text, expected_len", [
    ("", 0),
    ("<br><p></p>", 0),
    ("Hello WORLD!", 2),
    ("...!?!?!?", 0),
    ("zażółć gęślą jaźń", 3),
    ("the cat sat on the mat", 6),
])
def test_tokenize_cases(tokenizer, text, expected_len):
    assert len(tokenizer.tokenize(text)) == expected_len

def test_vocab_dedup(tokenizer):
    assert tokenizer.vocab(["aa bb", "bb cc"]) == {"aa", "bb", "cc"}

def test_min_length_filter():
    tok = Tokenizer(min_length=4)
    assert tok.tokenize("a bb ccc dddd eeeee") == ["dddd", "eeeee"]

def test_imdb_integration(tokenizer, imdb_sample):
    vocab = tokenizer.vocab(imdb_sample)
    assert len(vocab) > 500, f"za malo unikalnych tokenow: {len(vocab)}"
    print(f"\n[INSIGHT_DATA] Liczba unikalnych tokenow dla 20 recenzji: {len(vocab)}")

@pytest.mark.xfail(reason="Tokenizer nie wspiera jeszcze regex z grupowaniem")
def test_advanced_regex_unsupported():
    tok = Tokenizer()
    assert tok.tokenize("user@domain.com")[0] == "user@domain.com"
