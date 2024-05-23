from django.urls import *
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logindata/',logindata,name='logindata'),

    path('dashboard/',dashboard,name='dashboard'),

]