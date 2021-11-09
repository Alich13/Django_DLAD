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
    #images = models.ManyToManyField(Images, related_name='question', blank=True)

    def __str__(self):
        return str(self.question)


    def get_answers(self):
         return self.answer_list_set.all()


class Answer_list (models.Model):

    answer =models.CharField(max_length=200,null=True)
    definition = models.TextField(null=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"question: {self.question_id.question }," \
               f" answer: {self.answer},"



class Historique (models.Model) :

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(null=True)
    quiz =  models.IntegerField(null=False)
    Date = models.DateTimeField(auto_now=True, auto_now_add=False)
    time = models.TimeField(auto_now=True, auto_now_add=False)