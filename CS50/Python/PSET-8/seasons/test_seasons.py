from seasons import convert, inputdate
import pytest

def test_convert():
    assert convert(2020, 9, 23) == 1055520
    assert convert(2001, 10, 20) == 11010240

def test_inputdate():
    with pytest.raises(SystemExit):
        inputdate("23-Jan-2000")
    with pytest.raises(SystemExit):
        inputdate("22 Feb 2000")
    with pytest.raises(SystemExit):
        inputdate("")
