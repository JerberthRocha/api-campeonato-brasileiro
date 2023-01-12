from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from .models import Time, Jogador
from .serializers import JogadorSerializer, TimeSerializer, ElencoSerializer, DivisaoSerializer
from django.shortcuts import render
from rest_framework.response import Response
from django.utils.text import slugify
    

class TimeViewSet(viewsets.ModelViewSet):
    """Mostra todos as equipes que participam do Campeonato Brasileiro séries A e B."""
    queryset = Time.objects.all().select_related('divisao')
    serializer_class = TimeSerializer


class JogadorViewSet(viewsets.ModelViewSet):
    """Mostra todos os jogadores que participam do Campeonato Brasileiro séries A e B."""
    queryset = Jogador.objects.all().select_related('time')
    serializer_class = JogadorSerializer


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class ElencoViewSet(APIView):
    """Mostra o elenco completo da equipe informada por parâmetro."""
    def get(self, request, **kwargs):
        parametro = str(*kwargs.values())
        if parametro.isnumeric():
            elenco = Jogador.objects.filter(time__id__exact=int(parametro)).select_related('time')
        else:
            parametro = slugify(parametro)
            elenco = Jogador.objects.filter(time__slug__contains=parametro).select_related('time')

        serializer = ElencoSerializer(elenco, many=True)
        return Response(serializer.data)


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class DivisaoViewSet(APIView):
    """Mostra todos os atletas que jogam na divisão informada por parâmetro"""
    def get(self, request, **kwargs):
        parametro = slugify(str(*kwargs.values()))
        divisao = Jogador.objects.filter(time__divisao__slug=parametro).select_related('time')

        serializer = DivisaoSerializer(divisao, many=True)
        return Response(serializer.data)


@permission_classes((permissions.IsAuthenticatedOrReadOnly,))
class TimeDivisaoViewSet(APIView):
    """Mostra todos os atletas que jogam na divisão informada por parâmetro"""
    def get(self, request, **kwargs):
        parametro = slugify(str(*kwargs.values()))
        print(parametro)
        divisao = Time.objects.filter(divisao__slug=parametro).select_related('divisao')

        serializer = TimeSerializer(divisao, many=True)
        return Response(serializer.data)


def home(request):
    times = Time.objects.order_by('nome').select_related('divisao')
    contexto = {'times': times}
    return render(request, 'jogadores/pages/index.html', contexto)
