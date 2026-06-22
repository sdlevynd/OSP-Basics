from app.models import User


def test_password_hashing():
    user = User(email="john@email.com")

    user.set_password("secret123")

    assert user.password != "secret123"
    assert user.check_password("secret123")
    assert not user.check_password("wrong")

