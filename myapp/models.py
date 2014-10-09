from django.db import models
from djangotoolbox.fields import EmbeddedModelField, ListField

class Film(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    def __unicode__(self):
        return self.name
    
class Cinema(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    adress = models.TextField()
    def __unicode__(self):
        return self.name
    
class Session(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    film = models.ForeignKey(Film)
    cinema = models.ForeignKey(Cinema)
    
    def __unicode__(self):
        return self.cinema.name + " " + self.film.name

# Create your models here.
