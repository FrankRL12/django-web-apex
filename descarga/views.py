from django.shortcuts import render
from descarga.models import Descarga

# Create your views here.
def descarga(request):
    descarga=Descarga.objects.all()
    return render(request, 'templates/descarga.html',{'descargas': descarga})
