from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def index(request):
    context={
        'dojos':Dojo.objects.all(),
        'ninjas':Ninja.objects.all()
    }
    return render(request, 'index.html', context)

def createDojo(request):
    Dojo.objects.create(
        dojo_name=request.POST['dojo_name'], 
        dojo_city=request.POST['dojo_city'], 
        dojo_state=request.POST['dojo_state']
        )
    return redirect('/')

def createNinja(request):
    Ninja.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        dojo=request.POST['dojo']
        )
    return redirect('/')