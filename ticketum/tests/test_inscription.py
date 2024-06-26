import unittest
from main import db
from main.models import InscriptionModel as Inscription
from main.models import EventModel as Event
from main.models import GuestModel as Guest
from tests import BaseTestCase
from tests.constants import event_data_1, guest_data_1, inscription_data_1, inscription_data_2, inscription_data_3
from main.services import InscriptionService

class TestInscriptionController(BaseTestCase):
    """
    Test the InscriptionController controllers
    """

    def setUp(self):
        """
        Setup the test case and create the initial inscription data
        """
        super().setUp()
        self.client = self.app.test_client()

        # Create the initial event and guest in the database
        self.event = Event(**event_data_1)
        self.guest = Guest(**guest_data_1)
        db.session.add_all([self.event, self.guest])
        db.session.commit()

        # Create the initial inscription in the database
        self.inscription_1 = Inscription(**inscription_data_1)
        db.session.add(self.inscription_1)
        db.session.commit()

    def test_post_inscription(self):
        """
        Test the POST /events/{event_code}/inscriptions controller
        """
        inscription_data = {
            'name': 'Guest Name',
            'email': 'guestemail@example.com',
            'phone': '123456789',
            'dni': 123456789
        }
        response = self.client.post('/api/events/E001/inscriptions', json=inscription_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('status', response.json)
        self.assertIn('event_code', response.json)
        self.assertIn('guest_code', response.json)

    def test_get_inscription(self):
        """
        Test the GET /events/{event_code}/inscriptions/{guest_code} controller
        """
        response = self.client.get('/api/events/E001/inscriptions/G-0001')
        self.assertEqual(response.status_code, 200)
        self.assertIn('status', response.json)
        self.assertIn('event_code', response.json)
        self.assertIn('guest_code', response.json)

    def test_delete_inscription(self):
        """
        Test the DELETE /events/{event_code}/inscriptions/{guest_code} controller
        """
        response = self.client.delete('/api/events/E001/inscriptions/G-0001')
        self.assertEqual(response.status_code, 200)
        self.assertIn('', response.json)


class TestInscriptionService(BaseTestCase):
    '''
    Test the InscriptionService methods
    '''

    def setUp(self):
        '''
        Setup the test case and create the initial inscription data
        '''

        # Call the parent method
        super().setUp()

        # Create the initial inscriptions
        inscription_service = InscriptionService()

        # Create Inscription 1
        self.inscription_1 = inscription_service.create(**inscription_data_1)

        # Create Inscription 2
        self.inscription_2 = inscription_service.create(**inscription_data_2)

        # Create Inscription 3
        self.inscription_3 = inscription_service.create(**inscription_data_3)

    def test_create_inscription(self):
        '''
        Test create method of InscriptionService
        '''
        inscription_data = {
            'status': 'Confirmed',
            'event_id': 4,  # Replace with an actual event ID
            'guest_id': 4   # Replace with an actual guest ID
        }
        inscription_service = InscriptionService()
        inscription = inscription_service.create(**inscription_data)
        self.assertIsNotNone(inscription)
        self.assertEqual(inscription.status, 'Confirmed')

    def test_find_all_inscriptions(self):
        '''
        Test find_all method of InscriptionService
        '''
        inscription_service = InscriptionService()
        inscriptions = inscription_service.find_all()
        self.assertEqual(len(inscriptions), 3)

    def test_find_inscription_by_id(self):
        '''
        Test find_by_id method of InscriptionService
        '''
        inscription_service = InscriptionService()
        inscription = inscription_service.find_by_id(self.inscription_1.id)
        self.assertEqual(inscription.status, 'Confirmed')

    def test_update_inscription(self):
        '''
        Test update method of InscriptionService
        '''
        inscription_service = InscriptionService()
        updated_data = {
            'status': 'Canceled',
            'event_id': self.inscription_1.event_id,
            'guest_id': self.inscription_1.guest_id
        }
        updated_inscription = inscription_service.update(1, **updated_data)
        self.assertEqual(updated_inscription.status, 'Canceled')

    def test_delete_inscription(self):
        '''
        Test delete method of InscriptionService
        '''
        inscription_service = InscriptionService()
        result = inscription_service.delete(self.inscription_3.id)
        self.assertTrue(result)

        # Check that inscription has been deleted
        inscription = inscription_service.find_by_id(self.inscription_3.id)
        self.assertIsNone(inscription)

    

if __name__ == '__main__':
    unittest.main()

