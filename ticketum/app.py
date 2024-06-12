from main import create_app
from main import db
from config import Config

# Initialize the configuration
config = Config()
config.load_env_variables()

app = create_app()

app.app_context().push()

if __name__ == '__main__':
    # Database creation
    db.create_all()
    # Run the application
    app.run(debug=True, port=config.SV_PORT)