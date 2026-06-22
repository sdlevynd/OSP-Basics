from .extensions import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<User {self.id}, Email={self.email}>"

    def set_password(self, password):
        from .utils.hashing import hash_password
        self.password = hash_password(password)

    def check_password(self, password):
        from .utils.hashing import hash_password
        return self.password == hash_password(password)

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False, default=0.0)

    def __repr__(self):
        return f"Product: {self.name}"

