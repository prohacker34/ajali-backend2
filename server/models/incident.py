from . import db

class Incident(db.Model):
    __tablename__ = 'incidents'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    status = db.Column(db.String(50), default='under investigation')
    reporter_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    media = db.relationship("Media", back_populates="incident", cascade="all, delete-orphan")

    reporter = db.relationship('User', back_populates='incidents')  
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "reporter_id": self.reporter_id,
            "reporter_username": self.reporter.username if self.reporter else None,
            "media": [m.to_dict() for m in self.media]
        }

