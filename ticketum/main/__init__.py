from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from config_test import TestConfig
import os

# Initialize the ORM
db = SQLAlchemy()

# Initialize the migration engine
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)

    # Initialize the configuration
    config = config_class()
    config.load_env_variables()

    if isinstance(config, TestConfig):
        app.config['SQLALCHEMY_DATABASE_URI'] = config.DB_ENGINE
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS
        app.config['TESTING'] = config.TESTING
    else:
        db_full_path = config.DB_PATH + config.DB_NAME
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

        database_uri = config.DB_ENGINE + db_full_path
        print(f"Database URI: {database_uri}")
        app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.event_routes import event_bp
    from .routes.inscription_routes import inscription_bp

    app.register_blueprint(event_bp, url_prefix='/api')
    app.register_blueprint(inscription_bp, url_prefix='/api')

    return app
