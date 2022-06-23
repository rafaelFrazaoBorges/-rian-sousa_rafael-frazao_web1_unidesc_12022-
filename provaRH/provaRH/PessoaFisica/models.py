from django.db import models

class PessoaFisica(models.Model):
    cpf = models.CharField(max_length=20)
    rg = models.CharField(max_length=20)
    nome = models.CharField(max_length=20)
    sexo = models.CharField(max_length=20)
    dataNascimento = models.CharField(max_length=20)
