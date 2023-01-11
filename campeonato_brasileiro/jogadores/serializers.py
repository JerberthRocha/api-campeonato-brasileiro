from rest_framework import serializers
from .models import Jogador, Time, Campeonato


class CampeonatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campeonato
        exclude = ['id']


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ['nome']


class JogadorSerializer(serializers.ModelSerializer):
    time = TimeSerializer()
    class Meta:
        model = Jogador
        fields = ['id', 'nome', 'foto', 'time']


class ElencoSerializer(serializers.ModelSerializer):
    # time = TimeSerializer()
    class Meta:
        model = Jogador
        exclude = []