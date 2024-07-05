from rest_framework import serializers
from .models import Cliente, Categoria, Producto, Pedido, Reseña

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class ReseñaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reseña
        fields = '__all__'
