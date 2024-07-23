from typing import Any
from django.db import models

# Create your models here.
class Evento(models.Model):
    def __init__(self, nome, categoria, local=None, link=None):
        self.nome = nome
        self.categoria = categoria
        self.local = local
        self.link = link

aula_python = Evento('Aula de Python', 'Educação', 'Sala 1')
aula_js = Evento('Aula de JavaScript', 'Educação',  link='https://aula-de-js.com')
eventos = [
    aula_python, 
    aula_js,
    ]