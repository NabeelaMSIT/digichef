from django.http import HttpResponse
from models import Recipe
from django.shortcuts import render_to_response, get_object_or_404


def search(request):
	"""Search page"""
	return render_to_response('index.html')

def recipes(request):
	"""View of a list of recipes"""
	recipe_list = Recipe.objects.all().order_by('title')
	return render_to_response('recipe_list.html', {'recipe_list' : recipe_list})


def recipe_detail(request, recipe_id):
	"""View for a detailed look at a single recipe

		returns 404 error is recipe not found"""
	recipe = get_object_or_404(Recipe, pk=recipe_id)
	ingredient_list = recipe.ingredients.split("\n")
	return render_to_response('recipe_detail.html', {'recipe' : recipe, 'ingredient_list' : ingredient_list})
