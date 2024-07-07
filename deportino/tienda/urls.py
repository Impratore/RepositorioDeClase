from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, ProductoViewSet, ClienteViewSet, PedidoViewSet, ReseñaViewSet, RegistrarCliente

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'reseñas', ReseñaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('registrar/', RegistrarCliente.as_view(), name='registrar-cliente'),
]
