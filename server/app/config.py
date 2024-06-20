import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://user:password@localhost/flask_app_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

