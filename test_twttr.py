from twttr import shorten

def test_empty_string():
    assert shorten("") == ""

def test_no_vowels():
    assert shorten("bcdfg") == "bcdfg"

def test_all_vowels_lowercase():
    assert shorten("aeiou") == ""

def test_all_vowels_uppercase():
    assert shorten("AEIOU") == ""

def test_mixed_case():
    assert shorten("Hello World") == "Hll Wrld"

def test_numbers_and_symbols():
    assert shorten("H3ll0 W@rld!") == "H3ll0 W@rld!"

def test_long_text():
    input_text = "This is a longer test string with multiple VOWELS"
    expected = "Ths s  lngr tst strng wth mltpl VWLS"
    assert shorten(input_text) == expected
