import unittest
from datetime import datetime
from flask_testing import TestCase
from app import create_app
from config_test import TestConfig
from main import db


class BaseTestCase(TestCase):
    '''
    Base class for test cases
    '''
    def create_app(self):
        '''
        App creation using test configuration instance
        '''
        app = create_app(TestConfig)
        return app

    def setUp(self):
        '''
        Setup the test case
        '''
        db.create_all()
        db.session.commit()

    def tearDown(self):
        '''
        Tear down the test case
        '''
        db.session.remove()
        db.drop_all()