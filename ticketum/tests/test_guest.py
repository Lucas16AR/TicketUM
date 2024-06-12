import unittest
from main import db
from main.models import GuestModel as Guest
from tests import BaseTestCase
from tests.constants import guest_data_1, guest_data_2, guest_data_3
from main.services import GuestService


class TestGuestController(BaseTestCase):
    """
    Test the Guest controllers
    """

    def setUp(self):
        """
        Setup the test case and create the initial guest data
        """
        super().setUp()
        self.client = self.app.test_client()

        # Create the initial guests in the database
        guest_1 = Guest(**guest_data_1)
        guest_2 = Guest(**guest_data_2)
        guest_3 = Guest(**guest_data_3)

        # Add the guest data to the database
        db.session.add(guest_1)
        db.session.add(guest_2)
        db.session.add(guest_3)
        db.session.commit()

    def test_get_guests(self):
        """
        Test the GET /guests controller
        """
        response = self.client.get('/api/guests')
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json), 0)
        self.assertIn('name', response.json[0])

    def test_post_guest(self):
        """
        Test the POST /guests controller
        """
        guest_data = {
            'name': 'Test Guest',
            'email': 'testguest@example.com',
            'phone': '123456789',
            'dni': 123456789
        }
        response = self.client.post('/api/guests', json=guest_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)
        self.assertEqual(response.json['name'], 'Test Guest')

    def test_get_guest(self):
        """
        Test the GET /guests/<id> controller
        """
        response = self.client.get(f'/api/guests/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], guest_data_1['name'])

    def test_put_guest(self):
        """
        Test the PUT /guests/<id> controller
        """
        updated_data = {
            'name': 'Updated Guest',
            'email': 'updatedguest@example.com',
            'phone': '987654321',
            'dni': 987654321
        }
        response = self.client.put(f'/api/guests/1', json=updated_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], 'Updated Guest')

    def test_delete_guest(self):
        """
        Test the DELETE /guests/<id> controller
        """
        response = self.client.delete(f'/api/guests/1')
        self.assertEqual(response.status_code, 204)

        deleted_guest = Guest.query.get(1)
        self.assertIsNone(deleted_guest)

class TestGuestService(BaseTestCase):
    """
    Test the GuestService methods
    """

    def setUp(self):
        """
        Setup the test case and create the initial guest data
        """
        super().setUp()
        self.guest_service = GuestService()

        # Create the initial guests in the database
        self.guest_1 = self.guest_service.create(**guest_data_1)
        self.guest_2 = self.guest_service.create(**guest_data_2)
        self.guest_3 = self.guest_service.create(**guest_data_3)

    def test_create_guest(self):
        """
        Test the create method of GuestService
        """
        guest_data = {
            'name': 'Test Guest',
            'email': 'testguest@example.com',
            'phone': '123456789',
            'dni': 123456789
        }
        new_guest = self.guest_service.create(**guest_data)
        self.assertIsNotNone(new_guest)
        self.assertEqual(new_guest.name, 'Test Guest')

    def test_find_all_guests(self):
        """
        Test the find_all method of GuestService
        """
        guests = self.guest_service.find_all()
        self.assertGreater(len(guests), 0)
        self.assertEqual(guests[0].name, guest_data_1['name'])

    def test_find_guest_by_id(self):
        """
        Test the find_by_id method of GuestService
        """
        guest = self.guest_service.find_by_id(self.guest_1.id)
        self.assertEqual(guest.name, guest_data_1['name'])

    def test_update_guest(self):
        """
        Test the update method of GuestService
        """
        updated_data = {
            'name': 'Updated Guest',
            'email': 'updatedguest@example.com',
            'phone': '987654321',
            'dni': 987654321
        }
        updated_guest = self.guest_service.update(self.guest_1.id, **updated_data)
        self.assertEqual(updated_guest.name, 'Updated Guest')

    def test_delete_guest(self):
        """
        Test the delete method of GuestService
        """
        self.guest_service.delete(self.guest_1.id)
        deleted_guest = self.guest_service.find_by_id(self.guest_1.id)
        self.assertIsNone(deleted_guest)


if __name__ == '__main__':
    unittest.main()

