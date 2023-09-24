from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('map/', views.map_view, name='map'),
    path('api/calculate', views.calculate, name='calculate'),
    path('railway-sidings/', views.railway_siding_list, name='railway_siding_list'),
]
