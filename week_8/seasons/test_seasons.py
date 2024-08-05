from seasons import check_date, convert_to_mins
import pytest


def main():
    test_input()
    test_minutes()


def test_input():
    with pytest.raises(SystemExit):
        check_date("January 9, 2001")
    with pytest.raises(SystemExit):
        check_date("2020/10/10")
    with pytest.raises(SystemExit):
        check_date("2025-10-10")
    with pytest.raises(SystemExit):
        check_date("2020-15-10")
    with pytest.raises(SystemExit):
        check_date("2020-11-31")
    with pytest.raises(SystemExit):
        check_date("2019-02-29")


def test_minutes():
    assert convert_to_mins("2022-06-25") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert_to_mins("2021-06-25") == "One million, fifty-one thousand, two hundred minutes"


if __name__ == "__main__":
    main()