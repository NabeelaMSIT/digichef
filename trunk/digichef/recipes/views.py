from django.http import HttpResponse
from models import Recipe
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Q
from digichef.tagging.models import Tag, TaggedItem


def search(request):
	"""Search page"""
	if request.GET.get('submitted', ''):
		ingredient1 = request.GET.get('ingredient1', '')
		ingredient2 = request.GET.get('ingredient2', '')
		ingredient3 = request.GET.get('ingredient3', '')
		
		qset = (Q(name=ingredient1) | Q(name=ingredient2) | Q(name=ingredient3))
		search_ingreds = Tag.objects.filter(qset)

		# any
		recipes = TaggedItem.objects.get_union_by_model(Recipe, search_ingreds)
		#all
#		recipes = TaggedItem.objects.get_intersection_by_model(Recipe, search_ingreds)

		return recipe_list(request, recipes)

	else:
		all_ingreds = Tag.objects.all()
		return render_to_response('index.html', {'ingredients':all_ingreds})



def recipes_all(request):
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
	return render_to_response('recipe_detail.html', {'recipe' : recipe, 'ingredient_list' : ingredient_list})
