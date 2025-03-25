from django.db import models
from django.utils import timezone 

# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()
    salario = models.DecimalField(max_digits=30, decimal_places=2)
    turno = models.CharField(max_length=30)
    cargo = models.CharField(default="Funcionário",max_length=20, choices=(('Fucionário', 'Caixa'), ('Gerente', 'Gerente')))

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Produto(models.Model):
    nome = models.CharField(max_length=30)
    preco = models.DecimalField(max_digits=30, decimal_places=2)
    quantidade_estoque = models.CharField(max_length=30)
    codigo = models.CharField(max_length=30)
    validade = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.nome} '
