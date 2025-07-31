from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os

from server.models import db
from server.models.incident import Incident
from server.models.media import Media

incidents_bp = Blueprint('incidents_bp', __name__, url_prefix='/incidents')


@incidents_bp.route('/', methods=['GET'])
def get_incidents():
    incidents = Incident.query.all()
    return jsonify([incident.to_dict() for incident in incidents])


@incidents_bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    incident = Incident.query.get_or_404(id)
    return jsonify(incident.to_dict())


@incidents_bp.route('/', methods=['POST'])
def create_incident():
    title = request.form.get('title')
    description = request.form.get('description')
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')
    status = request.form.get('status')

    if not all([title, description, latitude, longitude, status]):
        return jsonify({"error": "Missing required fields"}), 400

    incident = Incident(
        title=title,
        description=description,
        latitude=str(latitude),
        longitude=str(longitude),
        status=status,
    )
    db.session.add(incident)
    db.session.commit()

    files = request.files.getlist('media')
    upload_folder = current_app.config['UPLOAD_FOLDER']
    os.makedirs(upload_folder, exist_ok=True)

    for file in files:
        if file.filename == "":
            continue

        filename = secure_filename(file.filename)
        filepath = os.path.join(upload_folder, filename)
        file.save(filepath)

        media_type = "video" if "video" in file.content_type else "image"

        media = Media(
            type=media_type,
            url=filename,
            incident_id=incident.id
        )
        db.session.add(media)

    db.session.commit()

    return jsonify(incident.to_dict()), 201


@incidents_bp.route('/<int:id>', methods=['PATCH'])
def update_incident(id):
    incident = Incident.query.get_or_404(id)
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    if 'type' in data:
        incident.type = data['type']
    if 'url' in data:
        incident.url = data['url']

    db.session.commit()
    return jsonify(incident.to_dict()), 200
