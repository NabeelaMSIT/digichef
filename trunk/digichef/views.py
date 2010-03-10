
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render_to_response, get_object_or_404

def homepage(request):
	loginform = AuthenticationForm()
	return render_to_response('index.html', {'ingredients':all_ingreds, 'loginform':loginform}, RequestContext(request))
