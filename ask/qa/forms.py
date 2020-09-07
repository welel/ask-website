from django import forms
from qa.models import Question, Answer
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from django.conf import settings


class AskForm(forms.ModelForm):
    '''Form of question asking'''
    class Meta:
        model = Question
        fields = ['title', 'text']
        widgets = {'text': forms.Textarea()}
        labels = {
            'title': 'Question title',
            'text': 'Question text'
        }


class AnswerForm(forms.ModelForm):
    '''Form of question answering'''
    class Meta:
        model = Answer
        fields = ['text']
        label = {'text': 'Answer text'}


class SignupForm(forms.ModelForm):
    '''Website registration form'''
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = { 
                'email': forms.EmailInput(), 
                'password' : forms.PasswordInput()
                }

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(
                    pk=self.instance.pk
                    ).filter(username=username).exists():
            raise ValidationError(
                    'Username "%s" is already exists.' % username
                    )
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        validate_password(password)
        password = make_password(password, salt=settings.SECRET_KEY)
        return password


class SigninForm(forms.ModelForm):
    '''Website login form'''
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {'password': forms.PasswordInput()}
    
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        password = make_password(password, salt=settings.SECRET_KEY)
        try:
            self.instance = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            raise ValidationError('Username or password is wrong')
        return self.cleaned_data

