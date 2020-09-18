from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, Page, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.forms import ValidationError
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from qa.forms import AskForm, AnswerForm, SignupForm, SigninForm
from qa.models import Question, Answer
from qa.shortcuts import paginate


@require_GET
def questions_list_all(request, *args, **kwargs):
    '''Renders a page with list of questions sorted by addition time.'''
    questions = Question.objects.new()
    paginator, page = paginate(request, questions)
    # Use reserve() routing new time
    paginator.baseurl = '/?page='
    return render(request, 'questions_list.html', { 
            'questions': page.object_list,
            'paginator': paginator, 
            'page': page,
            'user': request.user 
            })


def question_and_answers(request, *args, **kwargs):
    '''
    Renders a page of one question with a form for the answer
    and other answers, and manages POST request from the form.
    '''
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
        'form': form,
        'user': request.user
        })


@login_required(login_url='/signin/')
def question_add(request, *args, **kwargs):
    '''
    Renders a page with a form for adding a question
    and manages POST requests to the form.
    '''
    if request.method == 'POST':
        question = Question(author=request.user)
        form = AskForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form})


def signup(request, *args, **kwargs):
    '''
    Renders a page with a form for user registration
    and manages POST requests to the form.
    '''
    logout(request)
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})                     


def signin(request, *args, **kwargs):
    '''
    Renders a page with a form for login on the website
    and manages POST requests to the form.
    '''
    error = ''
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            user = authenticate(
                                request,
                                username=request.POST['username'],
                                password=request.POST['password']
                                )
            login(request, user)
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
