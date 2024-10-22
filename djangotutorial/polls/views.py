from django.shortcuts import render, get_object_or_404
from .models import Question

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
