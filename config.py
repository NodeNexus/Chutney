# config.py
import os
from dotenv import load_dotenv

load_dotenv()

# Update config.py to use SQLite
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///streeteats.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False