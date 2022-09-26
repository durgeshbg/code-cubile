from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.deposit(20)
    

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(7)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(20)
