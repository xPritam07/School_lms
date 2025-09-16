from flask import Flask
from controllers.config import Config
from mongoengine import connect

app = Flask(__name__)
app.config.from_object(Config)

# Connect to MongoDB here
connect(
    db='sikshasathidb',
    host=app.config['MONGODB_SETTINGS']['host']
)

# Now import models and routes
import models.model as models
import controllers.routes as routes

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=app.config['FLASK_DEBUG'])