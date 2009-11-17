from django.db import models
from tagging.models import Tag


# Create your models here.
class Recipe(models.Model):
	title = models.CharField(max_length=200)
	ingredients = models.TextField()
	instructions = models.TextField()
	
	def _get_tags(self):
		return Tag.objects.get_for_object(self)

	def _set_tags(self, tag_list):
		Tag.objects.update_tags(self, tag_list)

	tags = property(_get_tags, _set_tags)

	def __unicode__(self):
		return self.title
        

