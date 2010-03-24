#recipes/views.py

from django.http import HttpResponse
from models import Recipe
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Q
from digichef.tagging.models import Tag, TaggedItem
from digichef.recommender.managers import RecommenderManager
from django.template import RequestContext
from digichef.voting.models import Vote
from django.contrib.auth.models import User

from digichef import simplejson


import re

def stupid_search(request):
	"""Search page"""
	if request.GET.get('submitted', ''):#if this a form submit;-
		#load the results of the select boxes into variable
		ingredient1 = request.GET.get('ingredient1', '')
		ingredient2 = request.GET.get('ingredient2', '')
		ingredient3 = request.GET.get('ingredient3', '')
		
		qset = (Q(name=ingredient1) | Q(name=ingredient2) | Q(name=ingredient3))
		search_ingreds = Tag.objects.filter(qset)#get the actual tags, not just their names

		# any
		recipes = TaggedItem.objects.get_union_by_model(Recipe, search_ingreds)
		#all
#		recipes = TaggedItem.objects.get_intersection_by_model(Recipe, search_ingreds)

		return recipe_list(request, recipes)

	else:#it's not a form submit, show the empty form
		all_ingreds = Tag.objects.all() #the select boxes need to know what ingreds there are
		return render_to_response('index.html', {'ingredients':all_ingreds}, RequestContext(request))

def api_collab_search(request):
	if request.method == "POST":
		q = request.POST.get('q', None)
		if q is not None:
			return collab_search(request, q)
		else:
			assert False, request.POST

def api_similar_recipes(request, recipe_id):
	man = RecommenderManager()

	similar_recipes = man.get_by_relevance_to_tags(Recipe.objects.get(id=recipe_id).tags, Recipe.objects.exclude(id=recipe_id) ,0)
	similar_recipes.sort(reverse=True)
	similar_recipes = [{'title':	recipe.title,
						'url':		recipe.get_absolute_url(),
						'img_url':	recipe.image_url
					} for rating, recipe in similar_recipes[:5]]

	json = simplejson.dumps(similar_recipes)
	return HttpResponse(json, mimetype="application/json")
	
	

def collab_search(request, search_string):
	search_terms = [str(item.strip(',')) for item in re.split(r"[,; \t]*", search_string) if item]
	man = RecommenderManager()

	results = man.get_by_relevance_to_tags(search_terms, Recipe.objects.all(),0)

	results.sort(reverse=True)

	return recipe_list(request, [listing[1] for listing in results])


def recipes_all(request):
        """View all recipes"""
        recipeSet = Recipe.objects.all().order_by('title')
        return recipe_list(request, recipeSet)


def recipe_list(request, queryset):
	"""View of a list of recipes"""
	return render_to_response('recipe_list.html', {'recipe_list' : queryset})


def recipe_detail(request, recipe_id):
	"""View for a detailed look at a single recipe

		returns 404 error if recipe not found"""
	recipe = get_object_or_404(Recipe, pk=recipe_id)
	ingredient_list = recipe.ingredients.split("\n")
	score = Vote.objects.get_score(recipe)


#	similar_recipes = man.get_similar_items_from_model(recipe, User.objects.all(), Recipe, min_value=0)
#	similar_recipes = man.get_similar_items(recipe, User.objects.all(), Recipe.objects.all()[:500], min_value=0.1)
	return render_to_response('recipe_detail.html', locals(), RequestContext(request))












