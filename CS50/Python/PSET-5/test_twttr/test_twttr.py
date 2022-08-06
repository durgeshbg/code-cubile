from twttr import shorten


def test_shorten():
    assert shorten("Twitter") == "Twttr"


def test_default():
    assert shorten("") == ""
