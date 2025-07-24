from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

from .models import db
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from server.routes.base_routes import base  # 👈 import the new blueprint


jwt = JWTManager()


from .routes.user_routes import users_bp
from .routes.incident_routes import incidents_bp
from .routes.media_routes import media_bp
from .routes.auth_routes import auth_bp
from .routes.admin_routes import admin_bp


def create_app():
    app = Flask(__name__)


    app.config.from_object("config.Config")
    app.config["JWT_SECRET_KEY"]=os.getenv("JWT_SECRET_KEY")
    app.config["JWT_TOKEN_LOCATION"]=["headers"]

    print("🔥 Connected to:", app.config["SQLALCHEMY_DATABASE_URI"])



    db.init_app(app)
    Migrate(app, db)
    jwt.init_app(app)
    CORS(app)


    from .models import user, incident, media

    app.register_blueprint(users_bp)
    app.register_blueprint(incidents_bp)
    app.register_blueprint(media_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(base)



    return app



