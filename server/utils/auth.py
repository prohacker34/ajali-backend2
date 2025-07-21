from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta

def generate_token(identity, expires_in=3600):
    return create_access_token(identity=identity, expires_delta=timedelta(seconds=expires_in))

def hash_password(password):
    return generate_password_hash(password)

def verify_password(password, hashed):
    return check_password_hash(hashed, password)