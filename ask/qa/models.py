from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        '''Returns QuerySet of questions sorted by addition time.'''
        return self.order_by('-id')


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
    objects = QuestionManager()

    def get_url(self):
        '''Returns a url of the question.'''
        return '/question/' + str(self.id) + '/'


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
