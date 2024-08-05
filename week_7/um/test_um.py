from um import count


def main():
    test_lower_case()
    test_upper_case()
    test_different_symbols()
    test_spaces()
    test_um_word()


def test_lower_case():
    assert count("thanks, um, for everything") == 1


def test_upper_case():
    assert count("THIS, UM, WAS GOOD") == 1


def test_different_symbols():
    assert count("um?") == 1
    assert count("Um. Not, sure, um.") == 2


def test_spaces():
    assert count("you um are um so um") == 3


def test_um_word():
    assert count("yummy") == 0
    assert count("umbrage") == 0
    assert count("hum") == 0


if __name__ == "__main__":
    main()