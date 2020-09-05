from django import forms
from qa.models import Question, Answer

''' to-DO: 
* Make Profanity Checker in the future 
  https://www.youtube.com/watch?v=jvB2DpIN_u4
* Find suitable value of min/max length 
'''

class AskForm(forms.Form):
    title = forms.CharField(max_length=255, min_length=1)
    text = forms.CharField(widget=forms.Textarea, min_length=1)

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']
'''
    def save(self):
        answer = Answer(text=self.text,question=self.question)
        answer.save()
        return answer
'''

'''
class AnswerForm(forms.Form):
    def __init__(self, question=None, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        self.question = question

    text = forms.CharField(min_length=1)

    def save(self, question):
        answer = Answer(question=question, **self.cleaned_data)
        answer.save()
        return answer
'''
