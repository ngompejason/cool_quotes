from django.contrib import admin
from .models import *

# Register your models here.
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('verse', 'verse_ref','holy_book')
    search_fields = ('verse', 'user')  # Add a search bar
    list_filter = ('created_at',)  # Add filters for date
    ordering = ('-created_at',)  # Order quotes by most recent first

admin.site.register(Quote, QuoteAdmin)

class VoteAdmin(admin.ModelAdmin):
    list_display = ('vote_type', 'created_at')
    search_fields = ('vote_type',) 
    list_filter = ('created_at',)
    ordering = ('-created_at',)

admin.site.register(Vote, VoteAdmin)
