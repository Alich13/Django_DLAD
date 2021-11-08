from django.shortcuts import render
from django.http import JsonResponse
from learn.models import *
from django.contrib.auth.decorators import login_required
import json


def quiz_page(request,pk):
    object_list=Question.objects.get(pk=pk)
    return render(request=request,
                  template_name='quiz/quiz_page.html',context={"obj_list":object_list})

@login_required
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
            images =Images.objects.filter(component=correct_answer)


        images= [ [image.id ,image.name] for image in images ]
        random.shuffle(images)
        images = images[:q.nb_images]
        correct_answer_object= Answer_list.objects.get(answer=correct_answer)
        correct_answer_description=correct_answer_object.definition
        res =[str(q),answers,images,correct_answer,correct_answer_description]

        questions_dict[str(i)]=res
        print(images)



    return JsonResponse({
        'data': questions_dict,
    })

@login_required
def res_view(request,pk):
    data=[]
    if request.is_ajax() and request.method == 'POST' :
        data = request.POST
        user = request.user
        all_question_and_ans_str = data.dict()["all_questions"]
        all_quest_ans_dict = json.loads(all_question_and_ans_str)
        # {"question_id" : [question , [propositions ..] ,[images..] , correct_ans , description , the choice] }
        """
         returned a dicts with weird key but parsble
         must parse here dict
         get question q,images,answer,correct_answer,**description to be ploted ** and append it to the list results 
         calcuulate score
        """
        results = []
        for key, value in all_quest_ans_dict.items():
            question_id =int(key)
            question = value[0]
            answered = value[5]
            correct_ans =value[3]
            images=value[2]
            description = value[4]
            results.append({question_id:{"question":question,"answered":answered,"correct_answer":correct_ans,"images":images,"description":description}})




        """# save data in database
        # to use it afterward to in summary_history view
        # # # scores, users in models in viewresult
        """
        user_record = Historique( user=user, score=10,quiz=1)
        user_record.save()





        return JsonResponse({"user":user.username,"passed":True,"score":"to calculate","results":results})


