import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST

from .forms import AskForm, AnswerForm, SignupForm, SigninForm
from .models import Question, Answer
from core.shortcuts import paginate
from core.views import handle_view


logger = logging.getLogger('ask')


@handle_view
@require_GET
def questions_list_all(request, *args, **kwargs):
    '''Renders a page with list of questions sorted by addition time.'''
    questions = Question.objects.new()
    paginator, page = paginate(request, questions)
    # TODO: Use reserve() routing new time
    paginator.baseurl = '/?page='
    return render(request, 'questions_list.html', { 
            'questions': paginator.get_page(page),
            'paginator': paginator, 
            'page': page,
            'user': request.user 
            })


@handle_view
def question_and_answers(request, *args, **kwargs):
    '''
    Renders a page of one question with a form for the answer
    and users answers.
    '''
    question = get_object_or_404(Question, pk=int(kwargs['question_id']))
    answers = Answer.objects.filter(question=question)
    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
        'form': AnswerForm(),
        'user': request.user
        })


@handle_view
@require_POST
@login_required(login_url='/signin/')
def add_answer(request, *args, **kwargs):
    '''Handle an answer addition form from the question page.'''
    question = get_object_or_404(Question, pk=int(kwargs['question_id']))
    answer = Answer(question=question, author=request.user)
    form = AnswerForm(request.POST, instance=answer)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@handle_view
@login_required(login_url='/signin/')
def add_question(request, *args, **kwargs):
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


@handle_view
@require_POST
@login_required(login_url='/signin/')
def delete_question(request, *args, **kwargs):
    '''Deliting of the question and redirect on the main page.'''
    Question.objects.filter(
        pk=kwargs['question_id'],
        author=request.user
    ).delete()
    return HttpResponseRedirect('/')


@handle_view
@require_POST
@login_required(login_url='/signin/')
def delete_answer(request, *args, **kwargs):
    '''Deliting of the answer and redirect on question page.'''
    Answer.objects.filter(
        pk=kwargs['answer_id'],
        author=request.user
    ).delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@handle_view
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


@handle_view
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


@handle_view
def log_out(request, *args, **kwargs):
    logout(request)
    return HttpResponseRedirect('/')
