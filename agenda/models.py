from typing import Any
from django.db import models

# Create your models here.

class Categoria(models.Model):
        nome = models.CharField(max_length=255, unique=True)

        def __str__(self):
            return f'{self.nome} - {self.id}'


class Evento(models.Model):
    nome = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    
    local = models.CharField(max_length=255, blank=True)
    link = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return f'{self.nome} - {self.categoria} - {self.local} - {self.link}'
