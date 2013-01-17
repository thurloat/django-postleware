from django.utils import unittest
from django.test.client import Client

class PostResponseMiddleware(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_basic_response(self):
        response = self.client.post('/test1', {'foo': 'bar'})
        self.assertEqual(response['Cache-Control'], 'no-cache')

