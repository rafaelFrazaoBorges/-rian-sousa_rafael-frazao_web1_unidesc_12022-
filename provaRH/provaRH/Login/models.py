from django.db import models


class Login(models.Model):
    email = models.CharField(max_length=20)
    senha = models.CharField(max_length=20)
    permissao = models.CharField(max_length=20)