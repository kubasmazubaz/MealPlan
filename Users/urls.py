from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name = "index"),
    path('log_sign/', views.log_sign, name='log_sign'),
]