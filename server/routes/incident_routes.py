from flask import Blueprint, request, jsonify
from server.models import db
from server.models.incident import Incident

incidents_bp=Blueprint('incidents_bp', __name__, url_prefix='/incidents')

@incidents_bp.route('/', methods=['GET'])
def get_incidents():
    incidents=Incident.query.all()
    return jsonify([incident.to_dict() for incident in incidents])

@incidents_bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    incident=Incident.query.get_or_404(id)
    return jsonify(incident.to_dict())

@incidents_bp.route('/', methods=['POST'])
def create_incident():
    data = request.get_json()

    incident = Incident(
        title=data['title'],
        description=data['description'],
        latitude=data['latitude'],
        longitude=data['longitude'],
        status=data['status'],
    )

    db.session.add(incident)
    db.session.commit()

    return jsonify(incident.to_dict()),201

@incidents_bp.route('/<int:id>', methods=['PATCH'])
def update_incident(id):
    incident=Incident.query.get_or_404(id)
    data = request.get_json()

    if not data:
        return jsonify({'error':'No input data provided'}), 400

    if 'type' in data:
        incident.type=data['type']
    if 'url' in data:
        incident.url=data['url']

    db.session.commit()
    return jsonify(incident.to_dict()),200