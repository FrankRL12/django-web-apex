from django.contrib import admin
from .models import Temporada

# Register your models here.
class TemporadaAdmin(admin.ModelAdmin):
    list_display=('video', 'titulo', 'descripcion')
    readonly_fields=("creado", "actualizado")

admin.site.register(Temporada, TemporadaAdmin)