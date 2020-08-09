
from django.urls import path
from .views  import *
from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter


# Create a router and register our viewsets with it.
ROUTER = DefaultRouter(trailing_slash=False)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(ROUTER.urls)),
    url(r'^hotwrapper', GetHotBits.as_view(), name="hb"),
]
    