from django.db import models

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
    points= models.IntegerField(null=False)
    nb_images = models.IntegerField(null=False) # the number of images to be displayed
    #nb_answers
    images = models.ManyToManyField(Images, related_name='question', blank=True)


class Answer_list (models.Model):
    description= models.TextField()
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)

# add playes