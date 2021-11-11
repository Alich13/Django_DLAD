from django.shortcuts import render
from django.http import JsonResponse
from learn.models import *
from django.contrib.auth.decorators import login_required
import json
from django.db.models import F

def quiz_page(request,pk):
    object_list=Quiz.objects.get(pk=pk)
    return render(request=request,
                  template_name='quiz/quiz_page.html',context={"obj_list":object_list})

@login_required
def quiz_data_view(request,pk):

    questions_dict = {}
    question =[Quiz.objects.get(pk=pk)] #
    questions_list = random.choices(question, k=5) #number of questions per quiz

    for i,q in enumerate(questions_list):
        answers = []
        for a in q.get_answers():
            answers.append(a.answer)
        random.shuffle(answers)
        answers=answers[:q.nb_answers]

        correct_answer=random.choices(answers, k=1)[0] #on choisi une reponse au hazard

        type_ = q.type


        if type_=="microscopy":
            images= q.images.filter(microscopy=correct_answer)
        elif type_=="component":
            images =q.images.filter(component=correct_answer)
        elif type_=="organism":
            images =q.images.filter(organism=correct_answer)
        elif type_=="celltype":
            images =q.images.filter(cell_type=correct_answer)


        images= [ [image.id ,image.name] for image in images ]
        random.shuffle(images)
        images = images[:q.nb_images]
        correct_answer_object= Answer_list.objects.get(answer=correct_answer)
        correct_answer_description=correct_answer_object.definition
        res =[str(q),answers,images,correct_answer,correct_answer_description]
        questions_dict[str(i)]=res

    return JsonResponse({
        'data': questions_dict,
        'quiz_id':pk,
        'time': 5
    })






@login_required
def res_view(request,pk):
    """
    saves quiz questions and answers in database
    and return a json response to display results with JS
    """
    data=[]
    if request.is_ajax() and request.method == 'POST' :
        data = request.POST
        user = request.user
        all_question_and_ans_str = data.dict()["all_questions"]
        all_quest_ans_dict = json.loads(all_question_and_ans_str)
        results = []
        score = 0
        for key, value in all_quest_ans_dict.items():
            question_id =int(key)+1
            question = value[0]
            answered = value[5]
            correct_ans =value[3]
            images=value[2]
            description = value[4]
            results.append({question_id:{"question":question,"answered":answered,"correct_answer":correct_ans,"images":images,"description":description}})
            if answered==correct_ans :
                score+=1
        score=(score/len(all_quest_ans_dict.keys()))*100

        quiz_id=int(data.dict()["quiz_id"]) # or question_id
        quiz=Quiz.objects.get(pk=quiz_id)
        print(quiz.points)
        if score > 70:
            Profile.objects.filter(user=user).update(Total_points=F('Total_points')+quiz.points)
        user_record = Stat( user=Profile.objects.get(user=user), score=score, quiz=quiz)
        user_record.save()

        return JsonResponse({"user":user.username,"passed":True,"score":score,"results":results})


