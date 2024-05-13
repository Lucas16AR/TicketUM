from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Initialize the configuration
    config = Config()
    config.load_env_variables()

    print("PATH DE LA BASE DE DATOS: ", config.DB_PATH+config.DB_NAME)

    # Initialize the database
    if not os.path.exists(config.DB_PATH+config.DB_NAME):
        os.mknod(config.DB_PATH+config.DB_NAME)

    app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_ENGINE+config.DB_PATH+config.DB_NAME
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)    

    return app