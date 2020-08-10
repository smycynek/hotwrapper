from django.urls import path, include
from django.conf.urls import url
import hotwrapper.views

urlpatterns = [
    path("", hotwrapper.views.GetHotBits.as_view()),
    url(r'^', include('hotwrapper.urls')),
]
