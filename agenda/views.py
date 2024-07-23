from django.shortcuts import render
from django.http import HttpResponse
from agenda.models import eventos
from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse('Hello, World!')


def exibir_eventos(request):
    evento = eventos[0]
    return render(request=request, template_name="agenda/exibir_evento.html", context={'evento': evento})