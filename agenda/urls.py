from django.urls import path
from agenda.views import listar_eventos, exibir_eventos, participar_evento, hello

urlpatterns = [
    path('', hello, name="hello"),
    path("eventos/", listar_eventos, name="listar_eventos"),
    path("eventos/<int:id>/", exibir_eventos, name="exibir_evento"),
    path("participar/", participar_evento, name="participar_evento"),
]