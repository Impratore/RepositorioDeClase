from django.contrib import admin
from .models import Cliente, Categoria, Producto, Pedido, Reseña

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellidos', 'email', 'direccion', 'ciudad', 'codigo_postal', 'telefono']
    search_fields = ['nombre', 'apellidos', 'email']

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

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'fecha', 'direccion_entrega', 'ciudad_entrega', 'codigo_postal_entrega', 'pagado']
    list_filter = ['pagado', 'fecha']

@admin.register(Reseña)
class ReseñaAdmin(admin.ModelAdmin):
    list_display = ['producto', 'cliente', 'comentario', 'calificacion', 'fecha']
    list_filter = ['calificacion', 'fecha']
    search_fields = ['producto__nombre', 'cliente__nombre']
