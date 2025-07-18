

from flask import Blueprint, request, jsonify
from server.models import db
from server.models.user import User


users_bp = Blueprint('users_bp', __name__, url_prefix='/users')


@users_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


@users_bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())


@users_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()

    user = User(
        username=data['username'],
        email=data['email'],
    )
    user.set_password(data['password'])

    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201
