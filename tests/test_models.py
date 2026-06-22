from app.models import User, Product


def test_password_hashing():
    user = User(email="john@email.com")

    user.set_password("secret123")

    assert user.password != "secret123"
    assert user.check_password("secret123")
    assert not user.check_password("wrong")

def test_new_product():
    product = Product(name="test",price=2.5)
    assert product.name == "test"
    assert product.price == 2.5





