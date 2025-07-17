

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db


from .routes.user_routes import users_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")


    db.init_app(app)
    Migrate(app, db)


    from .models import user, incident, media


    app.register_blueprint(users_bp)
    app.register_blueprint(incidents_bp)
    app.register_blueprint(media_bp)

   

    return app
