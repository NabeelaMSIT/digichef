from django.conf.urls.defaults import *
import recipes.views
import settings


from django.views.generic.simple import *

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

    (r'^$', redirect_to, {'url': '/search/'} ),
    (r'^search/?$', recipes.views.stupid_search),
    (r'^search/(?P<search_string>.*).*$', recipes.views.collab_search),

#	(r'^accounts/', include('registration.backends.default.urls')),
	(r'^accounts/', include('registration.urls')),


    (r'^profiles/', include('profiles.urls')),

    (r'^recipe/(?P<recipe_id>\d+).*$', recipes.views.recipe_detail),

    (r'^recipes/?$', recipes.views.recipes_all),
)
