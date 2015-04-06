### A example search view ###
```
from django.db.models import Q
from django.shortcuts import render_to_response
from models import Book

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(title__icontains=query) |
            Q(authors__first_name__icontains=query) |
            Q(authors__last_name__icontains=query)
        )
        results = Book.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("books/search.html", {
        "results": results,
        "query": query
    })
```


### newforms is the better version of forms ###
```
from django import newforms as forms
```


## generate docs with epydoc ##
```
PYTHONPATH=/home/django/ DJANGO_SETTINGS_MODULE=myuni.settings epydoc --html --parse-only --docformat plaintext re -v -o /home/django/myuni/html --graph all myuni
```