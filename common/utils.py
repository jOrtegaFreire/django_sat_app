import hashlib

def password_hash(password):
    _hash=hashlib.new('sha256')
    _hash.update(password.encode())
    return _hash.hexdigest()

def password_verify(password,hash):
    _hash=hashlib.new('sha256')
    _hash.update(password.encode())
    return _hash.hexdigest()==hash

def ingress_status(status):
    if status==0:return 'Received'
    elif status==1:return 'Inspecting'
    elif status==2:return 'Awaiting Aproval'
    elif status==3:return 'Repairing'
    elif status==4:return 'Repaired'
    elif status==5:return 'Delivered to Client'
    elif status==6:return 'Pending Return'
    elif status==7:return 'Returned'

