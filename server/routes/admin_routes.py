from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.models import db, User

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


def is_admin(user_id):
    user = User.query.get(user_id)
    return user and getattr(user, "is_admin", False)

@admin_bp.route('/users', methods=['GET'])
@jwt_required()
def get_all_users():
    current_user_id = get_jwt_identity()
    if not is_admin(current_user_id):
        return jsonify({"error": "Admin access required"}), 403

    users = User.query.all()
    result = [{"id": u.id, "username": u.username, "email": u.email} for u in users]
    return jsonify(result), 200
