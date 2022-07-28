from plates import is_valid

def test_valid():
    assert is_valid('GOOD50') == True

def test_puntuation():
    assert is_valid('PI3.14') == False

def test_lenght():
    assert is_valid('BIGLENGTH') == False
    assert is_valid('A') == False

def test_number_between():
    assert is_valid('ASD78B') == False

def test_number_begin_with_0():
    assert is_valid('GOOD00') == False