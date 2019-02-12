from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    # Construct a dictionary for template engine
    # the boldmessage is the same as {{boldmessage}} in the template
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')