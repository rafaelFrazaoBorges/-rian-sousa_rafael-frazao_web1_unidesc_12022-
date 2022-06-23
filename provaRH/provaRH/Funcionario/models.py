from django.db import models

# Create your models here.

class Funcionario(models.Model):
    cpf = models.CharField(max_length=20)
    rg = models.CharField(max_length=20)
    nome = models.CharField(max_length=20)
    sexo = models.CharField(max_length=50)
    dataNascimento = models.CharField(max_length=20)
    carteiraTrabalho = models.CharField(max_length=30)
    salario = models.CharField(max_length=20)
    pis = models.CharField(max_length=20)