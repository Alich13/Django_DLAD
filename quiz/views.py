from django.shortcuts import render, redirect
from django.http import JsonResponse
import random
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from learn.models import *
from django.contrib import messages

def quiz_page(request,pk):
    object_list=Question.objects.get(pk=pk)
    return render(request=request,
                  template_name='quiz/quiz_page.html',context={"obj_list":object_list})

def quiz_data_view(request,pk):

    questions_dict = []
    question =[Question.objects.get(pk=pk)] #
    questions_list = random.choices(question, k=5)


    for q in questions_list:
        answers = []
        for a in q.get_answers():
            answers.append(a.answer)

        type = q.type
        answers=random.choices(answers,k=q.nb_answers)
        correct_answer=random.choices(answers, k=1)[0] #on choisi une reponse au hazard
        print(correct_answer)
        if type=="microscopy":
            images= Images.objects.filter(microscopy=correct_answer)[:q.nb_images]
        elif type=="component":
            images =Images.objects.filter(component=correct_answer)[:q.nb_images]

        images= [ image.name for image in images ]
        print (images)
        res =[answers,images,correct_answer]
        questions_dict.append({str(q):res})

    return JsonResponse({
        'data': questions_dict,
        'time': 15,
    })