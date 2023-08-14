from django.shortcuts import  render, redirect
from cars.models import Car
from cars.forms import CarForm
from django.contrib.auth.decorators import login_required

def car_home(request):
   url_search = request.GET.get('search')
   cars = Car.objects.all().order_by('-year')
   form = CarForm()
   if url_search:
      cars = Car.objects.filter(model__icontains=url_search)
   return render( request, 
                  'home.html', 
                  {'cars':cars, 'form':form})

@login_required
def create_car(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cars:home')
    else:
        form = CarForm()
        
    return render(request, "create_car.html", {"form": form})
    

