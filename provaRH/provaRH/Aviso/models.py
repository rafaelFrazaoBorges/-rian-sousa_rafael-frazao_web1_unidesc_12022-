from django.db import models

class Aviso(models.Model):
    matricula_avi = models.CharField(max_length=20)
    assunto_avi = models.CharField(max_length=20)
    data_avi = models.CharField(max_length=20)