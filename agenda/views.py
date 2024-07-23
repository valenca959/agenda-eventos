from django.shortcuts import render
from django.http import HttpResponse
from .models import eventos

# Create your views here.
def index(request):
    return HttpResponse('Hello, World!')


def exibir_eventos(request):
    evento = eventos[0]
    return HttpResponse(f'''
    <html><h1>EVENTO: {evento.nome}</h1>
    <p>Categoria: {evento.categoria}</p>
    <p>Local: {evento.local}</p>
    <p>Link: {evento.link}</p>
    </html>
    ''')