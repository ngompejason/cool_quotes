from django import forms
from .models import Quote

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["verse","holy_book","verse_ref"]
    
    def clean_holy_book(self):
        holy_book = self.cleaned_data["holy_book"]
        capitalize_title = ' '.join([word.capitalize() for word in holy_book.split()])
        
        return capitalize_title
    
