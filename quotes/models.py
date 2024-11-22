from django.db import models
from users.models import CustomUser
import uuid

# Create your models here.

class Quote(models.Model):
    # Foreign key to the user who added the quote
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='quote', 
        help_text="User who added the quote."
    )
    verse = models.TextField(
        help_text = "Enter the quote text here.",
        blank=False
    )
    verse_ref = models.CharField(
        max_length = 55,
        help_text = "Enter the reference (chapter:verse) for the quote.",
        blank = False
    )
    holy_book = models.CharField(
        max_length=55,
        help_text="Specify the name of the holy book.", 
        blank=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the quote was added."
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Date and time whn the quote was lst update."
    )
    
    class Meta:
        verbose_name = "Quote"
        verbose_name_plural = "Quotes"
        ordering = ["-created_at"]
        
    def __str__(self):
        return f'"{self.verse[:50]}" by {self.user.username} from {self.holy_book}'