from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    """Represent a question asked by a user.
    
    **Fieldes**
        text: a question text.
        added_at: datetime of question creation.
        author: fk to a user (author of a quesiton).
    
    """
    text = models.TextField(
        max_length=200,
        verbose_name='Question text'
    )
    added_at = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Question addition date-time'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Author of the question'
    )

    def __str__(self):
        return self.text[:100]
    
    def get_url(self):
        """Returns a url of the question.
        
        TODO: Refactor to a `get_absolute_url`.
        
        """
        return '/question/' + str(self.id) + '/'
        
    def to_json(self):
        """Converts to dict of json format."""
        return {   
            'id': self.pk,
            'text': self.text,
            'author': self.author.username,
            'date': self.added_at.strftime('%b %d, %Y')
        }
        
    class Meta:
        ordering = ['-added_at']


class Answer(models.Model):
    """Represents an answer to a question.
    
    **Fields**
        text: an answer text to a question.
        added_at: datetime of answer creation.
        question: fk to a question.
        author: fk to a user (author of an answer).

    """
    text = models.TextField(
        max_length=10000,
        verbose_name='Answer text'
    )
    added_at = models.DateTimeField(
        blank=True,
        auto_now_add=True,
        verbose_name='Answer addition date-time'
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name='The answering question'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Author of the answer'
    )
