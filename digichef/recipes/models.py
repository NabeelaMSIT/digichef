from django.db import models
from tagging.models import Tag


# Create your models here.
class Recipe(models.Model):
	"""The model for a recipe object"""
	title = models.CharField(max_length=200)
	ingredients = models.TextField()
	instructions = models.TextField(blank=True)
	image_url = models.TextField(blank=True)
	
	def _get_tags(self):
		"return all tags associated with this object (thus all ingredients in this recipe)"
		return Tag.objects.get_for_object(self)

	def _set_tags(self, tag_list):
		"set the ingredients to all the names in the tag_list"
		Tag.objects.update_tags(self, tag_list)

	tags = property(_get_tags, _set_tags)#properties map getters and setters to a variable

	def get_absolute_url(self):
		return "/recipe/%s/" % self.id

	def __unicode__(self):
		"Called implicitly when you try and print a Recipe object"
		return self.title
        

