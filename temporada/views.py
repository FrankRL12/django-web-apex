from django.shortcuts import render
from temporada.models import Temporada

# Create your views here.
def temporada(request):
    temporada=Temporada.objects.all()
    return render(request, 'templates/temporada.html',{'temporadas': temporada})
