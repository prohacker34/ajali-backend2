import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from run import app

from server.models import db
from models.user import User
from models.incident import Incident
from models.media import Media

def seed():
    with app.app_context():
        print("Clearing existing data...")


        db.session.query(Media).delete()
        db.session.query(Incident).delete()
        db.session.query(User).delete()
        db.session.commit()

        print("Seeding users...")

        sam = User(

            username='niki',
            email='samnikos@gmail.com'
        )
        sam.set_password('1234')

        jessica = User(

            username='jessi',
            email='jessicareeves@gmail.com'
        )
        jessica.set_password('456')

        db.session.add_all([sam, jessica])
        db.session.commit()

        print("Seeding incidents...")

        incident1 = Incident(
            title='Broken streetlight',
            description='Streetlight on 5th Ave is not working',
            user=sam
        )
        incident2 = Incident(
            title='Pothole on Main St',
            description='Large pothole causing traffic issues',
            user=jessica
        )
        db.session.add_all([incident1, incident2])
        db.session.commit()

        print("Seeding media...")

        media1 = Media(
            type='image',
            url='https://media.istockphoto.com/id/2176543563/photo/two-damaged-vehicles-in-car-accident-after-collision-on-city-street-road-safety-and-insurance.webp?a=1&b=1&s=612x612&w=0&k=20&c=2lCFto8Y_8SWokPFR12pCDl_SkXth-SBTjVkRfW32MI=',
            incident=incident1
        )
        media2 = Media(
            type='video',
            url='https://media.istockphoto.com/id/2216417792/photo/close-up-of-damaged-car-part-after-accident-showing-broken-metal-and-scratches.webp?a=1&b=1&s=612x612&w=0&k=20&c=gI8lW7vG6qFivLY7hyDRUzUV1-THzfA8ydxf4nHo9Io=',
            incident=incident2
        )
        db.session.add_all([media1, media2])
        db.session.commit()

        print("Seeding complete!")

if __name__ == "__main__":
    seed()
