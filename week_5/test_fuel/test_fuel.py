from fuel import convert, gauge
import pytest

def main():
    test_zero_division()
    test_value()
    test_for_e()
    test_for_f()
    test_correct()

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value():
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_for_e():
    assert gauge(1) == "E"

def test_for_f():
    assert gauge(99) == "F"

def test_correct():
    assert convert("1/4") == 25 and gauge(25) == "25%"


if __name__ == "__main__":
    main()