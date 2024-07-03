from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug', 'precio', 'cantidad', 'disponibilidad', 'creado', 'actualizado']
    list_filter = ['disponibilidad', 'creado', 'actualizado']
    list_editable = ['precio', 'cantidad', 'disponibilidad']
    prepopulated_fields = {'slug': ('nombre',)}
