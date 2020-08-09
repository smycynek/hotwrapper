from django.urls import path, include

from django.conf.urls import url
from django.contrib import admin

admin.autodiscover()

import hotwrapper.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hotwrapper.views.GetHotBits.as_view()),
    url(r'^', include('hotwrapper.urls')),
]
