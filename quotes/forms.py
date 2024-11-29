from django import forms
from .models import *

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["verse","holy_book","verse_ref"]
        
        widgets = {
            'verse': forms.Textarea(attrs={'class': 'form-textarea',}),
            'holy_book': forms.TextInput(attrs={'class': 'form-input',}),
            'verse_ref': forms.TextInput(attrs={'class': 'form-input',}),
        }
    
    def clean_holy_book(self):
        holy_book = self.cleaned_data["holy_book"]
        capitalize_title = ' '.join([word.capitalize() for word in holy_book.split()])
        
        return capitalize_title
    
            
    

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["user_report",]
        
        widgets = {
            'user_report': forms.Textarea(attrs={'class': 'form-textarea',})
        }
