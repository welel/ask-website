from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        '''Returns QuerySet of questions sorted by addition time'''
        return self.order_by('-id')

    def popular(self):
        '''Returns QuerySet of questions sorted by question raiting'''
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User,  on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='question_like_user')
    objects = QuestionManager()

    def get_url(self):
        return '/question/' + str(self.id) + '/'


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

