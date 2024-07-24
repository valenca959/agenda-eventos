from django.shortcuts import render
from agenda.models import Evento
from datetime import date
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.
def listar_eventos(request):
    eventos = Evento.objects.filter(data__gte=date.today()).order_by('data')
    return render(
        request=request,
        template_name="agenda/listar_eventos.html", 
        context={'eventos': eventos})
     



def exibir_eventos(request, id):
    evento = get_object_or_404(Evento, id=id)
    return render(
        request=request, 
        template_name="agenda/exibir_evento.html", 
        context={'evento': evento})


def participar_evento(request):
    evento_id = request.POST.get('evento_id')
    evento = get_object_or_404(Evento, id=evento_id)
    evento.participantes += 1
    evento.save()

    return HttpResponseRedirect(reverse('exibir_evento', args=(evento_id,)))

def hello(request):
    return HttpResponse("Hello World!")