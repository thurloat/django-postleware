from django.conf.urls import patterns
from postleware.views import TestView

urlpatterns = patterns('',
    (r'^test1$', TestView.as_view()),
)
