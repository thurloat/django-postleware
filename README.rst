# django-postleware

A simple django middleware class which injects a `Cache-Control: no-cache`
header onto POST responses.

# Why?

Mobile Webkit (iOS4+ and Android stock bowser) has a bug that causes it to 
cache similar POST requests when it clearly shouldn't. Rather than only caching
requests that have a specific `Cache-Control` header, it does the opposite and
caches the request unless the `no-cache` value is present in the POST response.

# Not working for you?

Let me know by opening an issue or pull request. This was enough for me, but I
have read around the webs that other devs needed to add additional headers to
the response before it would stop caching.
