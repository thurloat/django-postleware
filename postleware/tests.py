from django.http import HttpResponse
from django.utils import unittest
from django.test.client import Client
from postleware import PostResponseCachebusterMiddleware


class PostResponseMiddleware(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_header_added_when_necessary(self):
        # 'Cache-Control: no-cache' is added to POSTs
        response = self.client.post('/test1', {'foo':'bar'})
        self.assertEqual(response['Cache-Control'], 'no-cache')

        # 'Cache-Control' is NOT added to GETs
        response = self.client.get('/test1')
        self.assertFalse(response.has_header('Cache-Control'))

    def test_header_not_added_when_present(self):
        middleware = PostResponseCachebusterMiddleware()
        test_header_setting = 'test-setting'
        raw_response = HttpResponse()

        # 'Cache-Control' header isn't modified when present on POSTs
        request = MockRequest('POST')
        raw_response['Cache-Control'] = test_header_setting
        response = middleware.process_response(request, raw_response)
        self.assertEqual(response['Cache-Control'], test_header_setting)

        # 'Cache-Control' header isn't modified when present on GETs
        request = MockRequest('GET')
        raw_response['Cache-Control'] = test_header_setting
        response = middleware.process_response(request, raw_response)
        self.assertEqual(response['Cache-Control'], test_header_setting)


class MockRequest(object):
    def __init__(self, method=None):
        self.method = method
