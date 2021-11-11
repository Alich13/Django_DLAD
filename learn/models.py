from django.db import models
from django.contrib.auth.models import User
import random

# Create your models here.

class Images(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    microscopy = models.CharField(max_length=200)
    cell_type = models.CharField (max_length=200)
    component = models.CharField(max_length=200)
    organism = models.CharField (max_length=200)
    doi = models.CharField(max_length=200)


class Question(models.Model):
    question= models.TextField()
    type = models.CharField(max_length=200)
    imagefield = models.CharField(max_length=200,null=True)
    points= models.IntegerField(null=False)
    nb_images = models.IntegerField(null=False) # the number of images to be displayed
    nb_answers = models.IntegerField(null=False)
    time = models.IntegerField(null=True)
    images = models.ManyToManyField(Images, related_name='question', blank=True)

    def __str__(self):
        return str(self.question)

    def get_answers(self):
         return self.answer_list_set.all()

    # def get_images(self,type_,value):
    #     return self.objects.filter(images__component=value)


class Answer_list (models.Model):

    answer =models.CharField(max_length=200,null=True)
    definition = models.TextField(null=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"question: {self.question_id.question }," \
               f" answer: {self.answer},"



class profile (models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=200, null=True)
    profile_image = models.CharField(max_length=200,null=True)
    Total_points = models.IntegerField(default=0)

class stats (models.Model) :
    user = models.ForeignKey(profile, on_delete=models.CASCADE)
    score = models.IntegerField(null=True)
    quiz =  models.ForeignKey(Question, on_delete=models.CASCADE) #id of the quiz
    Date = models.DateTimeField(auto_now=True, auto_now_add=False)
    time = models.TimeField(auto_now=True, auto_now_add=False)