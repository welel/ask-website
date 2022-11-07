from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST

from .forms import AskForm, AnswerForm, SignupForm, SigninForm
from .models import Question, Answer


@require_GET
def questions_list_all(request, *args, **kwargs):
    """Render a page with list of questions sorted by addition time."""
    questions = Question.objects.all()[:15]
    return render(request, 'questions_list.html', { 
            'questions': questions,
            'user': request.user 
            }
    )


@require_POST
def load_questions(request, *args, **kwargs):
    """Retern a portion of questions on ajax request."""
    if request.is_ajax:
        start = request.POST.get('qusetions_num', '15')
        if start.isdigit():
            start = int(start)
        else:
            start = 15
        questions = Question.objects.all()[start:start+15]
        data = []
        for question in questions:
            data.append(question.to_json())
        return JsonResponse({'questions': data}, status=200)
    return JsonResponse({}, status = 500)


def question_and_answers(request, *args, **kwargs):
    """Render question details (answers and answering form).
    
    Renders a page of one question with a form for the answering
    and users' answers.
    
    """
    question = get_object_or_404(Question, pk=int(kwargs['question_id']))
    answers = Answer.objects.filter(question=question)
    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
        'form': AnswerForm(),
        'user': request.user
        }
    )


@require_POST
@login_required(login_url='/signin/')
def add_answer(request, *args, **kwargs):
    """Handle answer creation."""
    question = get_object_or_404(Question, pk=int(kwargs['question_id']))
    answer = Answer(question=question, author=request.user)
    form = AnswerForm(request.POST, instance=answer)
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required(login_url='/signin/')
def add_question(request, *args, **kwargs):
    """Render a question creation form and handle POST request."""
    if request.method == 'POST':
        question = Question(author=request.user)
        form = AskForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form})


@require_POST
@login_required(login_url='/signin/')
def delete_question(request, *args, **kwargs):
    """Deliting of the question and redirect on the main page."""
    Question.objects.filter(
        pk=kwargs['question_id'],
        author=request.user
    ).delete()
    return HttpResponseRedirect('/')


@require_POST
@login_required(login_url='/signin/')
def delete_answer(request, *args, **kwargs):
    """Deliting of the answer and redirect on question page."""
    Answer.objects.filter(
        pk=kwargs['answer_id'],
        author=request.user
    ).delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def signup(request, *args, **kwargs):
    """Render a user registration form and handle POST requests."""
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
    """Render a user login form and handle POST requests."""
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
        }
    )


def log_out(request, *args, **kwargs):
    logout(request)
    return HttpResponseRedirect('/')
