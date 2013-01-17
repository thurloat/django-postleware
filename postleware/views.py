from django.http import HttpResponse
from django.views.generic import View

class TestView(View):
    def post(self, request, *args, **kwargs):
        return HttpResponse('testing!')
