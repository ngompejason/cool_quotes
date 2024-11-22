from django.contrib import admin
from .models import Quote

# Register your models here.
class QuoteAdmin(admin.ModelAdmin):
    search_fields = ('verse', 'user')  # Add a search bar
    list_filter = ('created_at',)  # Add filters for date
    ordering = ('-created_at',)  # Order quotes by most recent first

admin.site.register(Quote, QuoteAdmin)
