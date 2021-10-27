from django.shortcuts import render
from django.http import JsonResponse
from learn.models import *
from datetime import datetime

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


def res_view(request,pk):
    data=[]
    if request.is_ajax() and request.method == 'POST' :
        data = request.POST
        user = request.user

        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
        print(data_.keys())


        """
         returned a dicts with weird key but parsble
         must parse here dict
         get question q,images,answer,correct_answer,**description to be ploted ** and append it to the list results 
         calcuulate score
        """



        """# save data in database
        # to use it afterward to in summary_history view
        # # # scores, users in models in viewresult
        """
        user_record = Historique( user=user, score=10,quiz=1)
        user_record.save()


        #our result must have this shape
        results =[
            {1:{"question":1,"answered":1,"correct_answer":1,"images":["1","2","3"]}},
            {2:{"question":2,"answered":1,"correct_answer":2,"images":["1","4","3"]}}
        ]


        return JsonResponse({"user":user.username,"passed":True,"score":"to calculate","results":results})


