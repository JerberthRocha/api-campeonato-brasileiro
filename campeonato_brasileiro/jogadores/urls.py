from rest_framework.routers import DefaultRouter
from .views import JogadorViewSet, TimeViewSet, ElencoViewSet, DivisaoViewSet, home
from django.urls import path

router = DefaultRouter()
router.register('jogadores', JogadorViewSet),
router.register('times', TimeViewSet), 
#TODO url de elenco -> /campeonato-brasileiro/elenco/<int:id> -> substitui na url o id pelo nome do clube
# router.register('campeonato', CampeonatoViewSet), 

urlpatterns = [
    path('home', home),
    # path('elenco/<int:pk>', ElencoViewSet.as_view(), name='elenco'),
    path('elenco/<str:time>', ElencoViewSet.as_view(), name='elenco'),
    path('jogadores/<str:divisao>', DivisaoViewSet.as_view(), name='divisao'),
]
