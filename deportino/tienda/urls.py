from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, CategoriaViewSet, ProductoViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]