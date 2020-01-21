from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from . import views
from .models import Choice, Question


def index(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html', {'questions': questions})

def show(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/show.html', {'question': question})

def vote(request, question_id):
    print(question_id)
    question = get_object_or_404(Question, pk=question_id)
    print(question)
    return render(request, 'polls/vote.html', {'question': question})

def add_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})