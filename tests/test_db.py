from app.extensions import db
from app.models import User

def test_db(app):
    assert app is not None

def test_create_user(app):
    with app.app_context():
        user = User(username="alice")

        db.session.add(user)
        db.session.commit()

        result = User.query.filter_by(username="alice").first()

        assert result is not None
        assert result.username == "alice"