from django.shortcuts import render, HttpResponse, redirect
from .models import User

def index(request):
    context = {
        "users" : User.objects.all()
        }
    return render(request, 'quotes/index.html', context)

def quotes(request):
    print(request.method)
    return render(request, 'quotes/quotes.html')

def users(request):
    if request.method == 'POST':
        User.objects.create(name=request.POST['name'],
        alias=request.POST['alias'], password=request.POST['password'])

        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
    return render(request, 'quotes/users.html')
