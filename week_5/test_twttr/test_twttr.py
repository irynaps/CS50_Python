from twttr import shorten

def test_lower():
    assert shorten("twitter") == "twttr"

def test_upper():
    assert shorten("BOHEMIAN") == "BHMN"

def test_combined():
    assert shorten("KIllER") == "KllR"

def test_numbers():
    assert shorten("4TH day") == "4TH dy"

def test_punctuation():
    assert shorten("Nice day. Today.") == "Nc dy. Tdy."