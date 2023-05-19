from django.contrib import admin
from .models import Descarga

# Register your models here.
class DescargaAdmin(admin.ModelAdmin):
    list_display=('imagen', 'titulo', 'descripcion')
    readonly_fields=("creado", "actualizado")
    
admin.site.register(Descarga, DescargaAdmin)