import unittest
from app import create_app

class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_user_profile(self):
        response = self.client.get('/user/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'User Profile', response.data)
