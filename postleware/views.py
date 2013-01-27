from django.http import HttpResponse
from django.views.generic import View

class TestView(View):
    def __init__(self, **kwargs):
        super(TestView, self).__init__(**kwargs)

        for method in self.http_method_names:
            setattr(self, method, self._default_response)

    def _default_response(self, request):
        return HttpResponse('testing!')
