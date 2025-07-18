

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db


from .routes.user_routes import users_bp
from .routes.media_routes import media_bp
from .routes.incident_routes import incidents_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    print("🔥 Connected to:", app.config["SQLALCHEMY_DATABASE_URI"])

    db.init_app(app)
    Migrate(app, db)


    from .models import user, incident, media


    app.register_blueprint(users_bp)
    app.register_blueprint(incidents_bp)
    app.register_blueprint(media_bp)



    return app
