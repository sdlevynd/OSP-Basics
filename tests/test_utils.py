from app.utils.hashing import hash_password
from app.utils.validation import presence_check, length_check, complexity_check

def test_hashing():
    assert hash_password("abcde") != hash_password("ABCDE")

def test_presence_check():
    assert presence_check("test")
    assert not presence_check("")
    assert presence_check([1,2,3])
    assert not presence_check([])

def test_length_check():
    assert length_check("abcde",5)
    assert not length_check("abcde",6)
    assert length_check("abcde",4)

def test_complexity_check():
    assert complexity_check("password")
    assert complexity_check("password", lower=True)
    assert not complexity_check("password", upper=True)
    assert not complexity_check("password", digit=True)
    assert not complexity_check("password", special=True)

    assert complexity_check("Password", lower=True, upper=True)
    assert not complexity_check("Password", lower=True, upper=True, digit=True)
    assert not complexity_check("Password", lower=True, upper=True, special=True)

    assert complexity_check("Password1", lower=True, upper=True, digit=True)
    assert not complexity_check("Password1", lower=True, upper=True, digit=True, special=True)

    assert complexity_check("Password1!", lower=True, upper=True, digit=True, special=True)

