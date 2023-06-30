from django.urls import path 
from cars.views import car_home

app_name ='cars'

urlpatterns = [
    path('', car_home, name='home'),    
]


