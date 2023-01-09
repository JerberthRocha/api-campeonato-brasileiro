from rest_framework import viewsets
from .models import Time, Jogador
from .serializers import JogadorSerializer, TimeSerializer
from django.shortcuts import render


class JogadorViewSet(viewsets.ModelViewSet):
    """Mostra os jogadores do Campeonato Brasileiro séries A e B."""
    queryset = Jogador.objects.order_by('-id')
    serializer_class = JogadorSerializer


class TimeViewSet(viewsets.ModelViewSet):
    """Mostra os times do Campeonato Brasileiro séries A e B."""
    queryset = Time.objects.order_by('-id').select_related('divisao')
    serializer_class = TimeSerializer


def home(request):
    return render(request, 'jogadores/pages/home.html')
