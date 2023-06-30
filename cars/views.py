from django.shortcuts import render
from .models import Car


def car_home(request):
    cars = Car.objects.all()
    return render(request, 'home.html', {'test':{'testando':'123'}})

