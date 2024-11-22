from django.urls import path
from quotes.views import *


urlpatterns = [
    path("", homepage, name="homepage"),
    path("quote/<uuid:quote_id>/", quote_detail, name="quote_detail"),
    path("post_quote", create_quote, name="create_quote"),
]
