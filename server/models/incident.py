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

    user = db.relationship('User', back_populates='incidents')  
    


