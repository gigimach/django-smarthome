from django.db import models
from django.contrib.auth.models import User

class Local(models.Model):
    descricao = models.TextField()
    cor = models.CharField(max_length=7)
    dono = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

class Ambiente(models.Model):
    descricao = models.TextField()
    cor = models.CharField(max_length=7)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

class Dispositivo(models.Model):
    descricao = models.TextField()
    online = models.BooleanField(default=True)
    ligado = models.BooleanField(default=False)
    cor = models.CharField(max_length=7)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descricao
