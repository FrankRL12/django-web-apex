from django.db import models

# Create your models here.
class Temporada(models.Model):
    video = models.FileField(upload_to='videos/')
    titulo= models.CharField(max_length=50)
    descripcion= models.CharField(max_length=100)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'temporada'
        verbose_name_plural = 'temporadas'

    def __str__(self):
        return self.titulo
