

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

from .models import db


from .routes.user_routes import users_bp
from .routes.media_routes import media_bp
from .routes.incident_routes import incidents_bp
from .routes.admin_routes import admin_bp




def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    app.config["JWT_SECRET_KEY"]=os.getenv("JWT_SECRET_KEY")
    app.config["JWT_TOKEN_LOCATION"]=["headers"]

    print("🔥 Connected to:", app.config["SQLALCHEMY_DATABASE_URI"])


    db.init_app(app)
    Migrate(app, db)

    jwt= JWTManager(app)


    from .models import user, incident, media


    app.register_blueprint(users_bp)
    app.register_blueprint(incidents_bp)
    app.register_blueprint(media_bp)
    app.register_blueprint(admin_bp)



    return app
