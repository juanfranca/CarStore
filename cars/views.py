from django.shortcuts import  render, redirect
from cars.models import Car
from cars.forms import CarForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class Car_home(ListView):
    template_name ='home.html'
    model = Car
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars

class Create_car(LoginRequiredMixin, CreateView):
    form_class = CarForm
    template_name = 'create_car.html'
    success_url = '/'
    

class Detail_car(DetailView):
    template_name = 'detail_car.html'
    model = Car
    context_object_name = 'cars'
    

class Update_car(UpdateView):
    template_name = 'edit_car.html'
    model = Car
    fields = '__all__'
    context_object_name = 'cars'
    success_url = '/'

class Delete_car(DeleteView):
    model = Car
    template_name = 'confirm_delete.html'
    success_url = '/'