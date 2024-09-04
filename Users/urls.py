from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_login, name='registration_login'),
    path('index/', views.index, name='index'),
]
