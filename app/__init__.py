from flask import Flask

from .extensions import db, migrate


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import main
    app.register_blueprint(main)

    # Import models so Flask-Migrate can discover them
    from . import models

    return app