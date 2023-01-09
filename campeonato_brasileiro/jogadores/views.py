# from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Time, Jogador

@api_view()
def times_view(request):
    times = Time.objects.all()
    saida = [{
        'time': time.nome,
        'divisao': time.divisao_id
    } for time in times]

    return Response(saida)

@api_view()
def jogadores_view(request):
    jogadores = Jogador.objects.all()
    saida = [{
        'nome': jogador.nome,
        'foto': jogador.foto,
        'id_time': jogador.time_id
    }for jogador in jogadores]

    return Response(saida)

# class APITimesView(APIView):
#     "Este endereço lista todos os times do campeonato brasileiro série A e B"
#     def get(self, request):
#         times = Time.objects.all()
#         serializer = TimeSerializer(times, many=True)

#         return Response(serializer.data)


