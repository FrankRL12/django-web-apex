from django.contrib import admin
from .models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display=('imagen', 'titulo', 'descripcion')
    readonly_fields=("creado", "actualizado")

admin.site.register(Blog, BlogAdmin)