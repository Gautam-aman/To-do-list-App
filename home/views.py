from django.shortcuts import render,redirect
from .models import *


# Create your views here.

def home(request):
    if request.method=="POST":
        data= request.POST
        name=data.get('name')
        
        t= task.objects.create(
            name=name
        )
        t.save()
        return redirect('/home/')
    queryset=task.objects.all()
    context= {'task':queryset}
    return render (request, 'home/templates/home.html', context)

def delete(request, id ):
    queryset = task.objects.get(id=id)
    queryset.delete()
    return redirect('/home/')
