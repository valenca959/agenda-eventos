from django.urls import path
from agenda.views import index, exibir_eventos

urlpatterns = [
    path('', index),
    path('eventos/', exibir_eventos),
]