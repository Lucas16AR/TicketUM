from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from config import Config
import os
from flask_migrate import Migrate

# Initialize the API of Flask Restful
api = Api()

# Initialize the ORM
db = SQLAlchemy()

# Initialize the migration engine
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Initialize the configuration
    config = Config()
    config.load_env_variables()

    db_full_path = config.DB_PATH+config.DB_NAME

    print(f"Database path: {db_full_path}")

    # Ensure the database directory exists
    if not os.path.exists(config.DB_PATH):
        try:
            os.makedirs(config.DB_PATH)
            print(f"Created directory: {config.DB_PATH}")
        except Exception as e:
            print(f"Error creating database directory: {e}")
            raise

    # Initialize the database file if it does not exist
    if not os.path.exists(db_full_path):
        try:
            open(db_full_path, 'a').close()
            print(f"Created database file: {db_full_path}")
        except Exception as e:
            print(f"Error creating database file: {e}")
            raise

    database_uri = config.DB_ENGINE+db_full_path

    print(f"Database URI: {database_uri}")

    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    migrate.init_app(app, db)

    import main.controllers as controllers

    api.add_resource(controllers.EventsResource, '/events')
    api.add_resource(controllers.EventResource, '/events/<int:event_id>')
    api.add_resource(controllers.GuestsResource, '/guests')
    api.add_resource(controllers.GuestResource, '/guests/<int:guest_id>')
    api.add_resource(controllers.InscriptionsResource, '/inscriptions')
    api.add_resource(controllers.InscriptionResource, '/inscriptions/<int:inscription_id>')

    api.init_app(app)

    return app