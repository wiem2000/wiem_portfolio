from django.shortcuts import render

# Create your views here.

def home(request):
    name="wiem"
    return render(request, 'index.html', {'name': name})
