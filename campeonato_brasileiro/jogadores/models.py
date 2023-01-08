from django.db import models


class Campeonato(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nome


class Time(models.Model):
    nome = models.CharField(max_length=40)
    divisao = models.ForeignKey(Campeonato, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self) -> str:
        return self.nome


class Jogador(models.Model):
    nome = models.CharField(max_length=30)
    foto = models.CharField(max_length=100)
    time = models.ForeignKey(Time, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        verbose_name_plural = 'Jogadores'