from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User

from .models import Answer, Question


class AskForm(forms.ModelForm):
    """Create a questin form."""

    class Meta:
        model = Question
        fields = ['text']
        widgets = {'text': forms.Textarea(
            attrs={'placeholder': 'You can start your question with \
                                  "What", "Why", "How", etc.'})
        }
        labels = {'text': 'Question text'}


class AnswerForm(forms.ModelForm):
    """Add an answer to a question form."""

    class Meta:
        model = Answer
        fields = ['text']
        widgets = {'text': forms.Textarea(attrs={
                            'placeholder': 'Write your answer here...'})}
        label = {'text': 'Answer text'}


class SignupForm(forms.ModelForm):
    """User registration form."""

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.confirm_password = forms.CharField(widget=forms.PasswordInput(), 
                                                label='Password Confirmation')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password',]
        widgets = {'email': forms.EmailInput(),
                   'password' : forms.PasswordInput()}
        labels = {'first_name': 'First name', 'last_name': 'Last name',
                  'username': 'Username', 'email': 'Email',
                  'password': 'Password'} 
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(
                                                username=username).exists():
            raise ValidationError(f'Username "{username}" is already exists.')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        validate_password(password)
        password = make_password(password, salt=settings.SECRET_KEY)
        return password


class SigninForm(forms.ModelForm):
    """Login to the website form."""

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {'password': forms.PasswordInput()}
    
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        password = make_password(password, salt=settings.SECRET_KEY)
        try:
            self.instance = User.objects.get(username=username,
                                             password=password)
        except User.DoesNotExist:
            raise ValidationError('Username or password is wrong!')
        return self.cleaned_data
