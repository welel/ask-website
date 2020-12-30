from django.db import models
from django.contrib.auth.models import User



class Question(models.Model):
    '''The main model, represents questions that asked by users.'''
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

    def get_url(self):
        '''Returns a url of the question.'''
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
    '''Represents answers of users on questions.'''
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
