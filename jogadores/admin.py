from django.contrib import admin
from .models import Time, Jogador,Campeonato

class JogadorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'time_id']
    list_display_links = ['id', 'nome']
    search_fields = ['id', 'nome']
    # list_editable = ('nome',)


class TimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'divisao_id']
    list_display_links = ['id', 'nome']
    search_fields = ['id', 'nome']


class CampeonatoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']


admin.site.register(Time, TimeAdmin)
admin.site.register(Jogador, JogadorAdmin)
admin.site.register(Campeonato, CampeonatoAdmin)
