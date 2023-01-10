from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from .models import Time, Jogador
from .serializers import JogadorSerializer, TimeSerializer, ElencoSerializer
from django.shortcuts import render
from rest_framework.response import Response


class JogadorViewSet(viewsets.ModelViewSet):
    """Mostra todos os jogadores do Campeonato Brasileiro séries A e B."""
    # queryset = Jogador.objects.order_by('-id')
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class ElencoViewSet(APIView):
    """Mostra o elenco completo de cada equipe do Campeonato Brasileiro séries A e B."""
    def get(self, request, pk):
        elenco = Jogador.objects.filter(time=pk).select_related('time')
        serializer = ElencoSerializer(elenco, many=True)
        return Response(serializer.data)
    

class TimeViewSet(viewsets.ModelViewSet):
    """Mostra todos as equipes que participam do Campeonato Brasileiro séries A e B."""
    queryset = Time.objects.all().select_related('divisao')
    serializer_class = TimeSerializer


def home(request):
    return render(request, 'jogadores/pages/home.html')

