from django.urls import path
from temporada import views

urlpatterns = [
    path('', views.temporada, name='temporada'),
]
