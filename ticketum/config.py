from dotenv import load_dotenv
import os

class Config:
    '''
    Configuration class to load the environment variables
    '''
    def __init__(self):
        load_dotenv()

    def load_env_variables(self):
        self.DB_NAME = os.getenv('DB_NAME')
        self.DB_USER = os.getenv('DB_USER')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD')
        self.DB_HOST = os.getenv('DB_HOST')
        self.DB_PORT = os.getenv('DB_PORT')
        self.DB_ENGINE = os.getenv('DB_ENGINE')
        self.DB_PATH = os.getenv('DB_PATH')
        self.SV_PORT = os.getenv('SV_PORT')
