from flask import Flask
from pymongo import MongoClient
from app.routes.user_routes import user_bp
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo_client = MongoClient(app.config["MONGO_URI"])
    app.db = mongo_client.get_database()

    # Register user routes
    app.register_blueprint(user_bp, url_prefix="/users")

    return app
