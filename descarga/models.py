from django.db import models

# Create your models here.
class Descarga(models.Model):
    imagen=models.ImageField(upload_to='descarga')
    titulo=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='descarga'
        verbose_name_plural='descargas'

    def __str__(self):
        return self.titulo
