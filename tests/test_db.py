from app.extensions import db
from app.models import User, Product

def test_db(app):
    assert app is not None

def test_create_user(app):
    with app.app_context():
        user = User(email="alice", password="test")

        db.session.add(user)
        db.session.commit()

        result = User.query.filter_by(email="alice").first()

        assert result is not None
        assert result.email == "alice"

def test_delete_user(app):
    assert True

def test_change_email(app):
    assert True

def test_change_password(app):
    assert True

def test_login(app):
    user = User(email="alice")
    user.set_password("test")

    db.session.add(user)
    db.session.commit()

    result = User.query.filter_by(email="alice").first()
    logged_in =  result.check_password("test")

    assert logged_in

def test_register(app):
    user = User(email="alice")
    user.set_password("test")

    db.session.add(user)
    db.session.commit()

    result = User.query.filter_by(email="alice").first()
    assert result.id == 1

    user = User(email="bob")
    user.set_password("test")

    db.session.add(user)
    db.session.commit()

    result = User.query.filter_by(email="bob").first()
    assert result.id == 2


def test_create_product(app):
    product = Product(name="test",price=2.5)

    db.session.add(product)
    db.session.commit()

    result = Product.query.filter_by(name="test").first()

    assert result is not None
    assert result.name == "test"#
    assert result.price == 2.5

def test_create_product_without_price(app):
    product = Product(name="test")

    db.session.add(product)
    db.session.commit()

    result = Product.query.filter_by(name="test").first()

    assert result is not None
    assert result.name == "test"#
    assert result.price == 0.0