from numb3rs import validate

def test_non_numbers():
    assert validate("cat") == False
