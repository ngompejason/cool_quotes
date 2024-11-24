from django.urls import path
from quotes.views import *


urlpatterns = [
    path("", homepage, name="homepage"),
    path("quote/<uuid:quote_id>/", quote_detail, name="quote_detail"),
    path("post_quote/", create_quote, name="create_quote"),
    path("edit_quote/<uuid:quote_id>/", edit_quote, name="edit_quote"),
    path("delete_quote/<uuid:quote_id>/", delete_quote, name="delete_quote"),
    
    path("q/<uuid:quote_id>/v/<vote_type>/", vote_quote, name="vote_quote"),
]
