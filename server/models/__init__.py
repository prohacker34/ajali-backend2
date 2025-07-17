from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import all model classes to bind them to metadata
from .user import User
from .incident import Incident
from .media import Media
