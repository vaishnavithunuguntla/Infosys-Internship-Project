from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurants/<str:city>/', views.restaurant_list, name='restaurant_list'),
]
