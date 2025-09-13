from dotenv import load_dotenv
import os

load_dotenv()

from app import app

app.config['MONGO_URI'] = os.getenv('MONGO_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')