from django.urls import path 
from cars.views import car_home, create_car

app_name ='cars'

urlpatterns = [
    path('', car_home, name='home'),
    path('create_car/', create_car, name='create_car'),       
]


