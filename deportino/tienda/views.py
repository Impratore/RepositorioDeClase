from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Usuario, Categoria, Producto
from .serializers import UsuarioSerializer, CategoriaSerializer, ProductoSerializer

# Definir ViewSets aquí.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [IsAuthenticated]

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]
