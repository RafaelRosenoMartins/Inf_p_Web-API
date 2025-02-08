from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LivroViewSet
from .views import AutorViewSet


router = DefaultRouter()
router.register(r'livros', LivroViewSet)  # Cria a rota /api/livro
router.register(r'autores', AutorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]