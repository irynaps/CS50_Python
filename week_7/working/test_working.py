from working import convert
import pytest


def main():
    test_wrong_format()
    test_wrong_hour()
    test_wrong_min()
    test_correct()


def test_wrong_format():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")


def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
        convert("9 AM tp 20 PM")


def test_wrong_min():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
        convert("9:00 AM to 5:60 PM")


def test_correct():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


if __name__ == "__main__":
    main()
