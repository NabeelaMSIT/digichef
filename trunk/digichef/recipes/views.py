from django.http import HttpResponse
from models import Recipe
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Q
from digichef.tagging.models import Tag, TaggedItem
from digichef.recommender.managers import RecommenderManager
from django.template import RequestContext


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

def collab_search(request, search_string):
	search_terms = [str(item.strip(',')) for item in search_string.split()]
	man = RecommenderManager()

	results = man.get_by_relevance_to_tags(search_terms,Recipe.objects.all(),0)

	results.sort()
	results.reverse()

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
	return render_to_response('recipe_detail.html', {'recipe' : recipe, 'ingredient_list' : ingredient_list})
