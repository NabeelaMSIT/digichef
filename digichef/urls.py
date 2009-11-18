from django.conf.urls.defaults import *

import recipes.views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
    # Example:
    # (r'^digichef/', include('digichef.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	(r'^admin/(.*)', admin.site.root),

    (r'^$', 'redirect_to', {'url': '/search/'} ),
    (r'^search/$', recipes.views.search),

    (r'^recipe/(?P<recipe_id>\d).*$', recipes.views.recipe_detail),
)
