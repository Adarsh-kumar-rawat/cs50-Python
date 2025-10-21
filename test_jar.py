import pytest
from jar import Jar

def test_init():
    # Default capacity
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    # Custom capacity
    jar2 = Jar(5)
    assert jar2.capacity == 5
    assert jar2.size == 0
    # Invalid capacity
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("large")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪"

def test_deposit():
    jar = Jar(5)
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(3)
    assert jar.size == 5
    # Deposit exceeding capacity
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2
    # Withdraw too many
    with pytest.raises(ValueError):
        jar.withdraw(3)
