from django.shortcuts import render, redirect
from django.http import JsonResponse
from learn.models import *

def quiz_page(request,pk):
    object_list=Question.objects.get(pk=pk)
    return render(request=request,
                  template_name='quiz/quiz_page.html',context={"obj_list":object_list})

def quiz_data_view(request,pk):

    questions_dict = {}
    question =[Question.objects.get(pk=pk)] #
    questions_list = random.choices(question, k=5)

    for i,q in enumerate(questions_list):
        answers = []
        for a in q.get_answers():
            answers.append(a.answer)
        random.shuffle(answers)
        answers=answers[:q.nb_answers]
        correct_answer=random.choices(answers, k=1)[0] #on choisi une reponse au hazard

        type_ = q.type
        if type_=="microscopy":
            images= Images.objects.filter(microscopy=correct_answer)
        elif type_=="component":
            images =Images.objects.filter(component=correct_answer)[:q.nb_images]


        images= [ image.name for image in images ]
        random.shuffle(images)
        images = images[:q.nb_images]
        correct_answer_object= Answer_list.objects.get(answer=correct_answer)
        correct_answer_description=correct_answer_object.definition
        res =[str(q),answers,images,correct_answer,correct_answer_description]

        questions_dict[str(i)]=res



    return JsonResponse({
        'data': questions_dict,
    })


def save_quiz_view(request, pk):
    if request.is_ajax():
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
        """
        returned a dicts with weird key but parsble 
        
        """
        print(data_.keys())
        print(data_['0[]'])
        print(data_['4[]'])
        # // calculate scores, store
        # scores, users in models in viewresult

        return JsonResponse({'passed': "yes"})
