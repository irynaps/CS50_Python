from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        jar = Jar(0)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(30)
    jar.deposit(15)
    assert jar.size == 15
    jar.deposit(10)
    assert jar.size == 25


def test_withdraw():
    jar = Jar(30)
    jar.deposit(25)
    jar.withdraw(10)
    assert jar.size == 15
    jar.withdraw(15)
    assert jar.size == 0


def test_withdraw_overflow():
    with pytest.raises(ValueError):
        jar = Jar(10)
        jar.withdraw(20)
