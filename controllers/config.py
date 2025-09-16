import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'False') == 'True'
    FLASK_APP = os.getenv('FLASK_APP', 'app.py')
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret')
    MONGODB_SETTINGS = {
        'host': os.getenv('MONGO_URI')
    }