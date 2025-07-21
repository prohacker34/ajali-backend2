# from server import create_app
# from server.models import db
# from server.models.user import User
# from server.models.incident import Incident
# from faker import Faker

# app = create_app()
# fake = Faker()

# def seed_data():
#     with app.app_context():
#         print("🔄 Dropping all tables...")
#         db.drop_all()

#         print("✅ Creating all tables...")
#         db.create_all()

#         print("🌱 Seeding users...")
#         users = []
#         for _ in range(3):
#             user = User(
#                 username=fake.user_name(),
#                 email=fake.email(),
#                 password_hash="password123"  # Use a hashed password in real apps
#             )
#             users.append(user)
#             db.session.add(user)

#         db.session.commit()

#         print("🌱 Seeding incidents...")
#         for user in users:
#             for _ in range(2):
#                 incident = Incident(
#                     title=fake.sentence(nb_words=5),
#                     description=fake.text(max_nb_chars=100),
#                     latitude=fake.latitude(),
#                     longitude=fake.longitude(),
#                     status="under investigation",
#                     reporter=user
#                 )
#                 db.session.add(incident)

#         db.session.commit()
#         print("✅ Done seeding!")

# if __name__ == "__main__":
#     seed_data()
