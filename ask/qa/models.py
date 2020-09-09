from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        '''Returns QuerySet of questions sorted by addition time'''
        return self.order_by('-id')


class Question(models.Model):
    text = models.TextField(max_length=200)
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = QuestionManager()

    def get_url(self):
        return '/question/' + str(self.id) + '/'


class Answer(models.Model):
    text = models.TextField(max_length=10000)
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

