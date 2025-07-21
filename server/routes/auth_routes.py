from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
<<<<<<< HEAD
from server.models import db, User
=======
from models import db, User
>>>>>>> 6a121d7176d8a01570d8a1c72737c5db31bed2f9
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 409

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid email or password"}), 401

    access_token = create_access_token(identity=user.id)
<<<<<<< HEAD
    return jsonify(access_token=access_token), 200
=======
    return jsonify(access_token=access_token), 200
>>>>>>> 6a121d7176d8a01570d8a1c72737c5db31bed2f9
