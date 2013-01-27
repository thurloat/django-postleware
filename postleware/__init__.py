try:
    VERSION = __import__('pkg_resources').get_distribution('django-postleware').version
except Exception, e:
    VERSION = "over 9000"

# Simple Middleware just bolts on the Cache-Control header.
#
class PostResponseCachebusterMiddleware(object):
    def process_response(self, request, response):
        if (request.method == 'POST' and
            not response.has_header('Cache-Control')):
            response['Cache-Control'] = 'no-cache'

        return response

