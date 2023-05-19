from django.db import models

# Create your models here.
class Blog(models.Model):
    imagen=models.ImageField(upload_to='blog')
    titulo=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=100)
    creado=models.DateTimeField(auto_now_add=True)
    actualizado=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name='blog'
        verbose_name_plural='blogs'

    def __str__(self):
        return self.titulo
