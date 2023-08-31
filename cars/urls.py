from django.urls import path 
from cars.views import Car_home, Create_car, Detail_car, Update_car, Delete_car

app_name ='cars'

urlpatterns = [
    path('', Car_home.as_view(), name='home'),
    path('create_car/', Create_car.as_view(), name='create_car'),
    path('detail_car/<int:pk>', Detail_car.as_view(), name='detail_car'),
    path('update/<int:pk>', Update_car.as_view(), name='update_car'),
    path('delete/<int:pk>', Delete_car.as_view(), name='delete_car'),             
]


