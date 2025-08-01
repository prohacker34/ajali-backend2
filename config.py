import os
print("Connected to DB:", os.getenv("DATABASE_URL"))


class Config:


    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL" )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "fallback-jwt-secret")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
