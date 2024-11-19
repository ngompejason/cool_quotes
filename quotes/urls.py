from django.urls import path
from quotes.views import *


urlpatterns = [
    path("", homepage, name="homepage"),
    path("ofatd/", ofatd, name="ofatd"),
]
