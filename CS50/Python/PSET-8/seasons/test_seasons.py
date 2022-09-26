from seasons import convert

def test_convert():
    assert convert(2020, 9, 23) == 1055520
    assert convert(2001, 10, 20) == 11010240
