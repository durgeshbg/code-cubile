from bank import value


def test_0():
    assert value("Hello Buddy") == 0


def test_20():
    assert value("Hi Lisa") == 20


def test_100():
    assert value("What's up!") == 100
