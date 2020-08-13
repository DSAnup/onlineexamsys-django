from django.shortcuts import render
from .models import *

from django.db.models import Avg, Count, Min, Sum

# Create your views here.

def index(request):
    ques = Questions.objects.all()
    ans = Answers.objects.all()
    qtime = Questions.objects.aggregate(Sum('question_time'))

    print(qtime)
    return render(request, 'home.html', {'ques': ques, 'ans': ans, 'time': qtime})