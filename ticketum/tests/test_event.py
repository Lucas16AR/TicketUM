import unittest
from datetime import datetime
from flask_testing import TestCase
from app import create_app
from config_test import TestConfig
from main import db
from tests import BaseTestCase
from main.models import EventModel as Event
from tests.constants import event_data_1, event_data_2, event_data_3
from main.services import EventService


class TestEventController(BaseTestCase):
    '''
    Test the Event controllers
    '''

    def setUp(self):
        '''
        Setup the test case and create the initial event data
        '''

        # Call the parent method
        super().setUp()

        # Create the initial event data
        event_1 = Event(**event_data_1)
        event_2 = Event(**event_data_2)
        event_3 = Event(**event_data_3)

        # Add the event data to the database
        db.session.add(event_1)
        db.session.add(event_2)
        db.session.add(event_3)
        db.session.commit()

    def test_get_events(self):
        '''
        Test the GET /events controller
        '''
        # Make a GET request to the /events route
        response = self.client.get('/api/events')
        self.assertEqual(response.status_code, 200)

        # Verify that the response is a list
        self.assertIsInstance(response.json, list)
        
        # Check that each item in the list has the expected keys
        for event in response.json:
            self.assertIn('code', event)
            self.assertIn('name', event)
            self.assertIn('description', event)
            self.assertIn('date', event)
            self.assertIn('location', event)
            self.assertIn('capacity', event)
            self.assertIn('total_inscriptions', event)

    def test_get_event(self):
        '''
        Test the GET /events/<event_code> controller
        '''
        # Get the first event from the database
        event = Event.query.first()

        # Make a GET request to the /events/<id> route
        response = self.client.get(f'/api/events/{event.event_code}')
        self.assertEqual(response.status_code, 200)
        # Verify that the response has the expected keys
        self.assertIn('code', response.json)
        self.assertIn('name', response.json)
        self.assertIn('description', response.json)
        self.assertIn('date', response.json)
        self.assertIn('location', response.json)
        self.assertIn('capacity', response.json)
        self.assertIn('total_inscriptions', response.json)


class TestEventServices(BaseTestCase):
    """
    Test the EventService methods
    """

    def setUp(self):
        """
        Setup the test case and create the initial event data
        """
        super().setUp()
        self.event_service = EventService()

        # Create the initial events in the database
        self.event_1 = self.event_service.create(**event_data_1)
        self.event_2 = self.event_service.create(**event_data_2)
        self.event_3 = self.event_service.create(**event_data_3)

    def test_create_event(self):
        """
        Test the create method of EventService
        """
        event_data = {
            'event_code': 'E004',
            'name': 'Test Event',
            'description': 'This is a test event.',
            'date': '2024-12-31 23:59:59',
            'location': 'Test Location',
            'capacity': 100
        }
        new_event = self.event_service.create(**event_data)
        self.assertIsNotNone(new_event)
        self.assertEqual(new_event.name, 'Test Event')

    def test_find_all_events(self):
        """
        Test the find_all method of EventService
        """
        events = self.event_service.find_all()
        self.assertGreater(len(events), 0)
        self.assertEqual(events[0].name, event_data_1['name'])

    def test_find_event_by_id(self):
        """
        Test the find_by_id method of EventService
        """
        event = self.event_service.find_by_id(self.event_1.id)
        self.assertEqual(event.name, event_data_1['name'])

    def test_update_event(self):
        """
        Test the update method of EventService
        """
        updated_data = {
            'event_code': 'E001',
            'name': 'Updated Event',
            'description': 'This is an updated event.',
            'date': '2024-12-31 23:59:59',
            'location': 'Updated Location',
            'capacity': 200
        }
        updated_event = self.event_service.update(self.event_1.id, **updated_data)
        self.assertEqual(updated_event.name, 'Updated Event')

    def test_delete_event(self):
        """
        Test the delete method of EventService
        """
        self.event_service.delete(self.event_1.id)
        deleted_event = self.event_service.find_by_id(self.event_1.id)
        self.assertIsNone(deleted_event)


if __name__ == '__main__':
    unittest.main()
