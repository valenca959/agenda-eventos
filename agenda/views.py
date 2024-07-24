from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from agenda.models import Evento
from datetime import date

# Create your views here.
def listar_eventos(request):
    eventos = Evento.objects.filter(data__gte=date.today()).order_by('data')
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

