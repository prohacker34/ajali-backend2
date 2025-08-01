
from server.models import db
from server import create_app

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ Tables created successfully.")



