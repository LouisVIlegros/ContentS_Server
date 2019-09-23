
import unittest

from base import BaseTestCase


class FlaskTestCase(BaseTestCase):

    # Ensure that search by id works correctly 
    def test_index(self):
        response = self.client.get('/search/5', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    # Ensure that search TRIE works correctly : should return a list of users that name or last name begin by "ba"
    def test_welcome_route_works_as_expected(self):
        response = self.client.post('/search', data=dict(search : "ba", dataType : "users", actionType : "autocomplete"))
        self.assertIn(b'Welcome to Flask!', response.data)

if __name__ == '__main__':
    unittest.main()
