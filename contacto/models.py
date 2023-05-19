from django.db import models

# Create your models here.
class Contacto(models.Model):
    imagen = models.ImageField(upload_to='contacto/', null=True, blank=True)
    nombre_completo = models.CharField(max_length=100)
    habilidades = models.TextField()
    ubicacion = models.CharField(max_length=100)
    facebook = models.URLField(max_length=200, null=True, blank=True)
    whatsapp = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)