from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name 
    = 'stuff-home'),
    path('suits/', views.suits, name = 'stuff-suits')
]