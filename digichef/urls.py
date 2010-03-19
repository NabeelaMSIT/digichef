#main urls.py

from django.conf.urls.defaults import *
import recipes.views
import core
import util
import settings


from django.views.generic.simple import *

from django.views.generic.create_update import create_object
import recipes.models

from voting.views import vote_on_object

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
'',
#'django.views.generic.simple',
    # Example:
    # (r'^digichef/', include('digichef.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	(r'^admin/(.*)', admin.site.root),

	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT, 'show_indexes': True}), 

    url(r'^$', 'core.views.home', name="home" ),

    (r'^search/?$', recipes.views.stupid_search),
    (r'^search/(?P<search_string>.*).*$', recipes.views.collab_search),
    url(r'^api/search$', recipes.views.api_collab_search, name="api_collab_search"),
    url(r'^api/json_tags$', 'util.views.json_tags', name="json_tags"),

#	(r'^accounts/', include('registration.backends.default.urls')),
	(r'^accounts/', include('registration.urls')),


    (r'^profiles/', include('profiles.urls')),

	url(r'^recipes/(?P<object_id>\d+)/(?P<direction>up|down|clear)vote/?$', vote_on_object, {'model':recipes.models.Recipe, 'template_object_name':'recipe', 'allow_xmlhttprequest':'true'}, name="recipe_voting"),
    (r'^recipe/(?P<recipe_id>\d+).*$', recipes.views.recipe_detail),

    (r'^recipes/new/?$', create_object, {'model': recipes.models.Recipe,'template_name': 'recipes/recipe_new.html', 'login_required': True}),

    (r'^recipes/?$', recipes.views.recipes_all),
)
