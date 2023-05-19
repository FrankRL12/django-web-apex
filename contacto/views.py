from django.shortcuts import render
from .models import Contacto

# Create your views here.
def contacto(request):
    perfil = Contacto.objects.first() 
    return render(request, 'templates/contacto.html', {'perfil': perfil})