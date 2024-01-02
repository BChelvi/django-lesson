# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from zoo.models import Animal


def say_hello(request):
    return HttpResponse('Hello World')


def say_hello_with_template(request):
    return render(request, 'hello.html', {'name': 'Cédric'})


def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'animal_list.html', {'animals': animals})
