from django.db import models

class Cliente(models.Model):
    dataCadastro = models.CharField(max_length=10)