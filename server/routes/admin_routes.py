from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.models import db, User,Incident

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
@admin_bp.route('/incidents/<int:incident_id>/status', methods=['PATCH'])
@jwt_required()
def update_incident_status(incident_id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user or not user.is_admin:
        return jsonify({"error": "Admins only"}), 403

    data = request.get_json()
    new_status = data.get('status')

    if not new_status:
        return jsonify({"error": "Status is required"}), 400

    incident = Incident.query.get(incident_id)
    if not incident:
        return jsonify({"error": "Incident not found"}), 404

    incident.status = new_status
    db.session.commit()

    return jsonify({"message": f"Incident status updated to '{new_status}'", "incident": {
        "id": incident.id,
        "title": incident.title,
        "status": incident.status
    }}), 200
