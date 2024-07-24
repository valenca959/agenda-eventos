from django.urls import path
from agenda.views import listar_eventos, exibir_eventos

urlpatterns = [
    path('', listar_eventos),
    path('eventos/', exibir_eventos),
]