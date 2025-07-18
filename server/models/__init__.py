from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


from .user import User
from .incident import Incident
from .media import Media
