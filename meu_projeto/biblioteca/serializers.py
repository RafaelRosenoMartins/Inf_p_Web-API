from rest_framework import serializers
from .models import Livro
from .models import Autor 

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class AutorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Autor
        fields = '__all__'
