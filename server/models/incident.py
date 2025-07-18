from . import db

class Incident(db.Model):
    __tablename__ = 'incidents'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    status = db.Column(db.String(50), default='under investigation')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='incidents')
    media = db.relationship('Media', back_populates='incident', lazy=True)

    def to_dict(self):
        return{
            "id":self.id,
            "title":self.title,
            "description":self.description,
            "lattitude":self.latitude,
            "longitude":self.longitude,
            "status":self.status
        }


