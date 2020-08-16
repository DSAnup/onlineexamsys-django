from django.shortcuts import render
from .models import *
from django.http import HttpResponse
import datetime
import random

from django.db.models import Avg, Count, Min, Sum

# Create your views here.

def index(request):
    ques = Questions.objects.all()
    ans = Answers.objects.all()
    qtime = Questions.objects.aggregate(Sum('question_time'))
    # qtime = str(qtime)
    # print(qtime)
    return render(request, 'home.html', {'ques': ques, 'ans': ans, 'time': qtime})

def sendans(request):
    ansval = request.POST.getlist('ansval[]')
    ans2 = Answers.objects.filter(currect_ans = 1)
    checkcurans = 0
    for i in ansval:
        x = i.split("_")
        for a in ans2:
            if int(x[0]) == a.id and x[1] == str(a.question_cat_id):
                checkcurans += 1
    # print(checkcurans)
    now = datetime.datetime.now()
    ques = Questions.objects.all()
    ans = Answers.objects.all()
    qcount = Questions.objects.all().count()
    return render(request, 'answercheck.html', {'ques': ques, 'ans': ans,
        'qcount': qcount, 'curans': checkcurans
        })