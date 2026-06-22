def hash_password(password):
    import hashlib
    s = 'salt'
    password_salt = password + s
    hashed = hashlib.sha256(password_salt.encode())
    return hashed.hexdigest()