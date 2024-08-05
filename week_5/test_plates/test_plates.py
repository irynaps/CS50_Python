from plates import is_valid

def test_numbers_only():
    assert is_valid("0000") == False

def test_too_short():
    assert is_valid("A") == False

def test_too_long():
    assert is_valid("AAAAAA22") == False

def test_numbers_in_middle():
    assert is_valid("AAA22A") == False

def test_first_number():
    assert is_valid("50CS") == False

def test_first_number_zero():
    assert is_valid("AA04") == False

def test_periods():
    assert is_valid("AA.22") == False

def test_spaces():
    assert is_valid("AA 22") == False

def test_punctuation():
    assert is_valid("AA!22") == False

def test_valid():
    assert is_valid("CS50") == True


if __name__ == "__main__":
    main()