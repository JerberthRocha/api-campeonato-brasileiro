from rest_framework import serializers
from .models import Jogador, Time, Campeonato


class JogadorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jogador
        fields = ['id', 'nome', 'foto', 'time']


class CampeonatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campeonato
        exclude = []


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        exclude = []

    divisao = CampeonatoSerializer()