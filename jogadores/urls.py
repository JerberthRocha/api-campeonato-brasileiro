from rest_framework.routers import DefaultRouter
from .views import JogadorViewSet, TimeViewSet, ElencoViewSet, \
                   DivisaoViewSet, TimeDivisaoViewSet, home
from django.urls import path

app_name = 'jogadores'

router = DefaultRouter()
router.register('jogadores', JogadorViewSet),
router.register('times', TimeViewSet), 

urlpatterns = [
    path('', home, name='home'),
    path('api/elenco/<str:time>', ElencoViewSet.as_view(), name='elenco'),
    path('api/jogadores/<str:divisao>', DivisaoViewSet.as_view(), name='divisao'),
    path('api/times/<str:campeonato>', TimeDivisaoViewSet.as_view(), name='campeonato'),
]
