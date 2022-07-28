from fuel import convert,gauge
import pytest

def test_convert_ValueError():
    with pytest.raises(ValueError):
        convert('cat/dog')
        convert('4/dog')
        convert('cat/2')
        convert('4/2')

def test_convert_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert('5/0')

def test_gauge_empty():
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'

def test_gauge_full():
    assert gauge(100) == 'F'
    assert gauge(99) == 'F'

def test_gauge():
    assert gauge(88) == '88%'
    assert gauge(25) == '25%'
