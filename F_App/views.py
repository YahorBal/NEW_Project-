from django.http import HttpResponse
from django.shortcuts import render

from F_App.models import Car


def hello_view(request):
    return HttpResponse("hello world ")

def create_car(request):
    car = Car(brand='demo', model='demo', color='demo')
    car.save()
    return HttpResponse(f'Yes!, New_car: {car.brand}')