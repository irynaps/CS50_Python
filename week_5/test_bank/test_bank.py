from bank import value

def test_hello():
    assert value("hello") == 0

def test_case():
    assert value("HELLO") == 0

def test_hey():
    assert value("hey") == 20

def test_h():
    assert value("how") == 20

def test_other():
    assert value("sup") == 100


if __name__ == "__main__":
    main()