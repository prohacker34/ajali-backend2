from . import db

class Media(db.Model):
    __tablename__ = 'media'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), nullable=False)
    url = db.Column(db.String, nullable=False)

    incident_id = db.Column(db.Integer, db.ForeignKey('incidents.id'), nullable=False)

    incident = db.relationship('Incident', back_populates='media')

    def to_dict(self):
        return{  
            
          "id":self.id,
          "type":self.type,
          "url":self.url
        }
