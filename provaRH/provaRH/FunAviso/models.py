from django.db import models

class FunAviso(models.Model):
    mensagem = models.CharField(max_length=20)