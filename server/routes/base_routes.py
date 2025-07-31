
from flask import Blueprint, jsonify

base = Blueprint('base', __name__)

@base.route("/")

def home():
    return "Hello from Flask + Waitress!"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
