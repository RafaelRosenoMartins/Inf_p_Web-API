from django.db import models

# Create your models here.

# Aqui foi criado um tabela Livro com 3 variáveis.

class Livro(models.Model):   
    titulo = models.CharField(max_length=100)
    autor  = models.CharField(max_length=100)
    publicado_em = models.DateField()

    def __str__(self):  # 
        return self.titulo
    
# Models.Model ela serve para transformar a classe em uma tabela no banco.
# DateFiel() ele armazena a data da máquina

# Makemigrations converte o model python em código SQL
# Migrate aplica o código SQL ao banco de dados.

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    nascimento = models.DateField()

    def __str__(self):
        return self.nome