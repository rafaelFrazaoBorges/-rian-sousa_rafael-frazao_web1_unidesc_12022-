from django.db import models

class Agendamento(models.Model):
    matricula = models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    cep = models.CharField(max_length=20)