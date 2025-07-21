from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

from .models import db
from flask_jwt_extended import JWTManager

jwt = JWTManager()

# Import all blueprints
from .routes.user_routes import users_bp


def create_app():
    app = Flask(__name__)
    
    # Load config (from config.py)
    app.config.from_object("config.Config")
    app.config["JWT_SECRET_KEY"]=os.getenv("JWT_SECRET_KEY")
    app.config["JWT_TOKEN_LOCATION"]=["headers"]

    print("🔥 Connected to:", app.config["SQLALCHEMY_DATABASE_URI"])


    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)
    jwt.init_app(app)


    from .models import user, incident, media

    # Register Blueprints
    app.register_blueprint(users_bp)
    # app.register_blueprint(incidents_bp)
    # app.register_blueprint(media_bp)



    return app



