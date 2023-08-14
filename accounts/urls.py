from django.urls import path

from .views import SignUp 

app_name = 'register'

urlpatterns = [ 
    path('register/', SignUp.as_view(), name="signup"),
]