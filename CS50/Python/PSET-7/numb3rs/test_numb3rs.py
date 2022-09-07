from numb3rs import validate, byte1, byte2, byte3, byte4

def test_non_numbers():
    assert validate("cat") == False

def test_number():
    assert validate("122.13.14.36") == True
