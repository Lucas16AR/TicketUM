from dotenv import load_dotenv
import os

class Config:
    '''
    Configuration class to load the environment variables
    '''
    def __init__(self):
        load_dotenv()

    def load_env_variables(self):
        '''
        Get the environment variables
        '''
        self.DB_NAME = os.getenv('DB_NAME')
        self.DB_USER = os.getenv('DB_USER')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD')
        self.DB_HOST = os.getenv('DB_HOST')
        self.DB_PORT = os.getenv('DB_PORT')
        self.DB_ENGINE = os.getenv('DB_ENGINE')
        self.DB_PATH = os.getenv('DB_PATH')
        self.SV_PORT = os.getenv('SV_PORT')
        self.MAIL_SERVER = os.getenv('MAIL_SERVER')
        self.MAIL_PORT = os.getenv('MAIL_PORT')
        self.MAIL_USE_TLS = os.getenv('MAIL_USE_TLS')
        self.MAIL_USERNAME = os.getenv('MAIL_USERNAME')
        self.MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
