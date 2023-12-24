from django.urls import path
from app import views

app_name = "app"

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('databases', views.databases, name="databases"),
    path('searchdb', views.searchdb, name='searchdb'),
]
