from rest_framework.routers import DefaultRouter
from django.urls import include
from django.conf.urls import url
from .views import *

# Create a router and register our viewsets with it.
ROUTER = DefaultRouter(trailing_slash=False)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(ROUTER.urls)),
    url(r'^hotwrapper', GetHotBits.as_view(), name="hb"),
]
