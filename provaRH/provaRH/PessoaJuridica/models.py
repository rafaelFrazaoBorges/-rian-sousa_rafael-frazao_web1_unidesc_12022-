from django.db import models

class PessoaJuridica(models.Model):
    cnpj = models.CharField(max_length=15)
    razaoSocial = models.CharField(max_length=13)
    representanteLegal = models.CharField(max_length=8)