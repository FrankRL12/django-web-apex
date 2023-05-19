from django.urls import path
from descarga import views


urlpatterns = [
    path('', views.descarga, name='descarga'),
]
