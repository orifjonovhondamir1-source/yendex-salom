from django.urls import path
from .views import *

urlpatterns = [

    path('home', home, name='home'),
    path('logo/', logo, name='logo'),
    path('salom/', salom, name='salom'),
    path('', reklama, name='reklama'),
    path("chiqish/", chiqish , name="chiqish"),                            
    path("detail/<int:tovar_id>/", detail, name="detail"),
    path("loyiha", loyiha, name="loyiha"),  
    path("login/", login , name="login"),                            
    path("yolhat/", yolhat, name="yolhat")
]