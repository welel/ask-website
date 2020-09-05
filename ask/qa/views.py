from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, Page, EmptyPage
from django.shortcuts import render, get_object_or_404
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm

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
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save(question)
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

def question_add(request, *args, **kwargs):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            return HttpResponseRedirect(question.get_url())
    else:
        form = AskForm()
    return render(request, 'ask.html', {
        'form': form
        })

