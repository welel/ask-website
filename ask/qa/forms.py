from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

''' to-DO: 
* Make Profanity Checker in the future 
  https://www.youtube.com/watch?v=jvB2DpIN_u4
* Find suitable value of min/max length 
'''

class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']
        widgets = {'text': forms.Textarea()}
    # link user with question

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = { 
                'email': forms.EmailInput(), 
                'password' : forms.PasswordInput()
                }
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise ValidationError('Username "%s" is already exists.' % username)
        return username

class SigninForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {'password': forms.PasswordInput()}
    
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        try:
            self.instance = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            raise ValidationError('Username or password is wrong')
        return self.cleaned_data


