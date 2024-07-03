from rest_framework import serializers
from .models import User, Category, Product, Cliente, Pedido, Reseña

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'address', 'phone_number']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'slug', 'image', 'description', 'price', 'available', 'stock', 'created', 'updated']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'apellidos', 'email', 'direccion', 'ciudad', 'codigo_postal', 'telefono']

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['id', 'cliente', 'fecha', 'direccion_entrega', 'ciudad_entrega', 'codigo_postal_entrega', 'pagado']

class ReseñaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reseña
        fields = ['id', 'producto', 'cliente', 'comentario', 'calificacion', 'fecha']