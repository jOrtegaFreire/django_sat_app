import hashlib

def password_hash(password):
    _hash=hashlib.new('sha256')
    _hash.update(password.encode())
    return _hash.hexdigest()

def password_verify(password,hash):
    _hash=hashlib.new('sha256')
    _hash.update(password.encode())
    return _hash.hexdigest()==hash

