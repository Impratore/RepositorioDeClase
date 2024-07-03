from django.contrib import admin
from .models import User, Category, Product, Cliente, Pedido, Reseña

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Reseña)
