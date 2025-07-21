from flask import Blueprint, request, jsonify
from server.models import db
from server.models.media import Media

media_bp = Blueprint('medias_bp',__name__,url_prefix='/media')


@media_bp.route('/', methods= ['GET'])
def get_medias():
    medias=Media.query.all()
    return jsonify([media.to_dict() for media in medias])

@media_bp.route('/<int:id>', methods=['GET'])
def get_media(id):
    media=Media.query.get_or_404(id)
    return jsonify(media.to_dict())

@media_bp.route('/', methods=['POST'])
def create_media():
    data = request.get_json()

    media=Media(
        type=data['type'],
        url=data['url'],
    )
    db.session.add(media)
    db.session.commit()

    return jsonify(media.to_dict()),201

@media_bp.route('/<int:id>', methods=['PATCH'])
def update_media(id):
    media = Media.query.get_or_404(id)
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    if 'type' in data:
        media.type = data['type']
    if 'url' in data:
        media.url = data['url']

    db.session.commit()
    return jsonify(media.to_dict()), 200