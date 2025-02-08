from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Livro
from .serializers import LivroSerializer
from .models import Autor
from .serializers import AutorSerializer

class LivroViewSet(viewsets.ModelViewSet):  # Cria automaticamente os endpoinsts (CRUD)
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer # Aq ele vai converte para JSON

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    
