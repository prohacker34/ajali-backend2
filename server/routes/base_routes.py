
from flask import Blueprint, jsonify

base = Blueprint('base', __name__)

@base.route("/")
def index():
    return jsonify({"message": "Ajali backend is live!"}), 200
