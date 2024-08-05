from lines import check_command_line, read_file
import pytest

def main():
    file_not_found()
    test_first()
    test_second()


def file_not_found():
    with pytest.raises(FileNotFoundError):
        read_file("test_three.py")

def test_first():
    assert read_file("test_one.py") == 2

def test_second():
    assert read_file("test_two.py") == 5


if __name__ == "__main__":
    main()

