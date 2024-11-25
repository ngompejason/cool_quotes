from django.db import models
from users.models import CustomUser
import uuid
from django.urls import reverse

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
    
    def upvote_count(self):
        return self.votes.filter(vote_type = 1).count()
    
    def downvote_count(self):
        return self.votes.filter(vote_type = -1).count()
    
    def score(self):
        return self.upvote_count() - self.downvote_count()
    
    class Meta:
        verbose_name = "Quote"
        verbose_name_plural = "Quotes"
        
        
    def get_absolute_url(self):
        return reverse("quote_detail", kwargs={"quote_id": self.id})
    
        
    def __str__(self):
        return f'"{self.verse[:50]}" by {self.user.username} from {self.holy_book}'
    
    
    def get_user_vote(self, user):
        if user.is_authenticated:
            vote = self.votes.filter(user=user).first()
            return vote.vote_type if vote else None
        return None


class Vote(models.Model):
    UPVOTE = 1
    DOWNVOTE = -1
    VOTE_CHOICES = [
        (UPVOTE, 'Upvote'),
        (DOWNVOTE, 'Downvote'),
    ]
    
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        help_text="User who added the vote."
    )
    quote = models.ForeignKey(
        Quote,
        on_delete=models.CASCADE,
        related_name='votes',
        help_text="The quote voted"
    )
    vote_type = models.SmallIntegerField(choices=VOTE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Vote"
        verbose_name_plural = "Votes"

    def __str__(self):
        return f"{self.user.username} - {self.vote_type}"
    

class Report(models.Model):

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
        )
    quote = models.ForeignKey(
        Quote,
        on_delete=models.CASCADE,
        related_name="reports"
        )
    user_report = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"

    def __str__(self):
        return f'{self.user_report[:50]}'

    # def get_absolute_url(self):
    #     return reverse("Report_detail", kwargs={"pk": self.pk})


