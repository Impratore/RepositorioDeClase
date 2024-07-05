from rest_framework import viewsets
from .models import Categoria, Producto, Cliente, Pedido, Reseña
from .serializers import CategoriaSerializer, ProductoSerializer, ClienteSerializer, PedidoSerializer, ReseñaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ReseñaViewSet(viewsets.ModelViewSet):
    queryset = Reseña.objects.all()
    serializer_class = ReseñaSerializer
