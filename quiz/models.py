from django.db import models

"""
Les relations se déclarent dans la classe qui contient la clé étrangère.
"""

"""
# Create your models here.
#----test_models---------------#
class Artist(models.Model): #herite de models.Model
    name = models.CharField(max_length=200, unique=True)
#CREATE TABLE store_artist ( "id" serial NOT NULL PRIMARY KEY, "name" varchar(200)
# NOT NULL UNIQUE );

class Contact(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)


class Album(models.Model):
    reference = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    picture = models.URLField()
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)

class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)
    album = models.OneToOneField(Album ,on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
"""
#-------------------------------------test models end --------------------------------#

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