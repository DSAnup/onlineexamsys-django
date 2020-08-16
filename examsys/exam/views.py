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
    n = random.random()
    ansval = request.POST.getlist('ansval[]')
    #print(ansval)
    ans2 = Answers.objects.filter(currect_ans = 2)
    checkcurans = 0
    for i in ansval:
        x = i.split("_")
        #print(x[0], x[1], n)
        for a in ans2:
            # checkcurans += 1
            print( x[1], a.question_cat_id, x[0], a.id)
            print(type(a.question_cat_id))
            if int(x[0]) == a.id and x[1] == str(a.question_cat_id):
                print('hello')
                checkcurans += 1
    print(checkcurans)
    now = datetime.datetime.now()
    ques = Questions.objects.all()
    ans = Answers.objects.all()
    return render(request, 'answercheck.html', {'ques': ques, 'ans': ans,})
    # subject = request.POST['subject']
    # message = request.POST['message']
    # Query.objects.create(
    #     name = name,
    #     email = email,
    #     subject = subject,
    #     message = message
    # ).save()
    # messages.success(request, 'Subsciption successfully completed')