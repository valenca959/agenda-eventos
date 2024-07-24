from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from agenda.models import Evento

# Create your views here.
def listar_eventos(request):
    eventos = Evento.objects.all()
    return render(
        request=request,
        template_name="agenda/listar_eventos.html", 
        context={'eventos': eventos})
     



def exibir_eventos(request):
    evento = {
        'nome': 'teste',
        'categoria': 'teste',
        'local': 'teste',
    }
    return render(
        request=request, 
        template_name="agenda/exibir_evento.html", 
        context={'evento': evento})

