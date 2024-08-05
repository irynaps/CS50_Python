from numb3rs import validate


def test_format():
    assert validate(r"255.255.255.0") == True
    assert validate(r"255.255.255") == False
    assert validate(r"255.255") == False
    assert validate(r"255") == False

def test_range():
    assert validate(r"255.3.6.28") == True
    assert validate(r"275.3.6.28") == False
    assert validate(r"255.275.6.28") == False
    assert validate(r"255.3.275.28") == False
    assert validate(r"255.3.6.275") == False