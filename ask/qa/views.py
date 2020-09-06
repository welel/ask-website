from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, Page, EmptyPage
from django.shortcuts import render, get_object_or_404
from qa.models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.forms import ValidationError
from qa.forms import AskForm, AnswerForm, SignupForm, SigninForm

def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return paginator, page

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def questions_list_all(request, *args, **kwargs):
    questions = Question.objects.new()
    paginator, page = paginate(request, questions)
    # Use reserve() routing new time
    paginator.baseurl = '/?page='
    return render(request, 'questions_list.html', { 
            'questions': page.object_list,
            'paginator': paginator, 
            'page': page 
            })

def questions_list_popular(request, *args, **kwargs):
    questions = Question.objects.popular()
    paginator, page = paginate(request, questions)
    # Use reserve() routing new time
    paginator.baseurl = '/popular/?page='
    return render(request, 'questions_list.html', { 
            'questions': page.object_list,
            'paginator': paginator, 
            'page': page 
            })

def question_and_answers(request, *args, **kwargs):
    question_id = int(kwargs['article_id'])
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == 'POST':
        answer = Answer(question=question, author=request.user)
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            form.save()
    else:
        form = AnswerForm()

    try:
        answers = Answer.objects.filter(question=question)
    except Answer.DoesNotExist:
        answers = []

    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
        'form': form
        })

# redirect if user isn't authntcatwetwetw
def question_add(request, *args, **kwargs):
    if request.method == 'POST':
        question = Question(author=request.user)
        form = AskForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        form = AskForm()
    return render(request, 'ask.html', {
        'form': form
        })

def signup(request, *args, **kwargs):
    if request.method == 'POST':
        form = SignupForm(request.POST, instance=User())
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def signin(request, *args, **kwargs):
    error = ''
    if request.method == 'POST':
        form = SigninForm(request.POST, instance=User())
        if form.is_valid():
            login(request, form.instance)
            return HttpResponseRedirect('/')
        else:
            error = 'Username or password is incorrect'
    form = SigninForm()
    return render(request, 'signin.html', {
        'form': form,
        'error': error
        })

def log_out(request, *args, **kwargs):
    logout(request)
    return HttpResponseRedirect('/')
