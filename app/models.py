from .extensions import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<User {self.id}>"

    def set_password(self, password):
        from .utils.hashing import hash_password
        self.password = hash_password(password)

    def check_password(self, password):
        from .utils.hashing import hash_password
        return self.password == hash_password(password)