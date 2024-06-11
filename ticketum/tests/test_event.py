import unittest
from datetime import datetime
from flask_testing import TestCase
from app import create_app
from config_test import TestConfig
from main import db
from tests import BaseTestCase


class TestEventRoutes(BaseTestCase):
    '''
    Test the EventController routes
    '''

    def test_get_events(self):
        '''
        Test the GET /events route
        '''
        # Create a test event
        event_data = {
            'event_code': 'E001',
            'name': 'Test Event',
            'description': 'This is a test event.',
            'date': '2024-12-31 23:59:59',
            'location': 'Test Location',
            'capacity': 100
        }
        self.client.post('/api/events', json=event_data)

        response = self.client.get('/api/events')
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json), 0)
        self.assertIn('name', response.json[0])

    def test_post_event(self):
        '''
        Test the POST /events route
        '''
        event_data = {
            'event_code': 'E001',
            'name': 'Test Event',
            'description': 'This is a test event.',
            'date': '2024-12-31 23:59:59',
            'location': 'Test Location',
            'capacity': 100
        }
        response = self.client.post('/api/events', json=event_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)
        self.assertEqual(response.json['name'], 'Test Event')

if __name__ == '__main__':
    unittest.main()
