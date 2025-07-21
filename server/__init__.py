from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db
from flask_jwt_extended import JWTManager

jwt = JWTManager()

# Import all blueprints
from .routes.user_routes import users_bp
from .routes.incident_routes import incidents_bp
from .routes.media_routes import media_bp  
from .routes.auth_routes import auth_bp
from .routes.admin_routes import admin_bp

def create_app():
    app = Flask(__name__)
    
    # Load config (from config.py)
    app.config.from_object("config.Config")
    print("🔥 Connected to:", app.config["SQLALCHEMY_DATABASE_URI"])

    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)
    jwt.init_app(app)

    # Import models (to register with SQLAlchemy before migrations)
    from .models import user, incident, media

    # Register Blueprints
    app.register_blueprint(users_bp)
    app.register_blueprint(incidents_bp)
    app.register_blueprint(media_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)

    return app



