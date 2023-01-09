from rest_framework.routers import DefaultRouter
from .views import JogadorViewSet, TimeViewSet, home
from django.urls import path

router = DefaultRouter()
router.register('jogadores', JogadorViewSet), 
router.register('times', TimeViewSet), 
# router.register('campeonato', CampeonatoViewSet), 

urlpatterns = [
    path('', home),
]
