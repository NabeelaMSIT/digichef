from django.db import models

# Create your models here.
class Recipe(models.Model):
    title= models.CharField(max_length=200)
    ingredients = models.TextField()
    ingredients = models.TextField()
    def __unicode__(self):
        return self.title
        

