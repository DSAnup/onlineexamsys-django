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
    y = []
    for i in ansval:
        x = i.split("_")
        y.append(x[1])

    from collections import Counter
    z = Counter(y)
    d = 0
    for u in z.most_common():
        anc = Answers.objects.filter(question_cat_id= u[0], currect_ans=1).count()
        if int(u[1]) == anc:
            d += 1
    ques = Questions.objects.all()
    ans = Answers.objects.all()
    qcount = Questions.objects.all().count()
    return render(request, 'answercheck.html', {'ques': ques, 'ans': ans,
        'qcount': qcount, 'curans': d
        })