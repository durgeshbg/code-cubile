from numb3rs import validate, byte1, byte2, byte3, byte4

def test_non_numbers():
    assert validate("cat") == False

def test_number():
    assert validate("122.13.14.36") == True

def test_byte1():
    assert byte1("234") == True
    assert byte1("278") == False

def test_byte2():
    assert byte2("234") == True
    assert byte2("278") == False

def test_byte3():
    assert byte3("234") == True
    assert byte3("278") == False

def test_byte4():
    assert byte4("234") == True
    assert byte4("278") == False
