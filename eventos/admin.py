from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    list_display = ['nome', 'endereco', 'capacidade']

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'palestrante', 'horario', 'evento']

@admin.register(Inscricao)
class InscircaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'inscrito_em', 'evento']

@admin.register(Relatorio)
class RelatorioAdmin(admin.ModelAdmin):
    list_display = ['presentes', 'observacoes', 'evento']


class AtividadesInline(admin.TabularInline):
    model = Atividade
    extra = 1

class RelatorioInline(admin.TabularInline):
    model = Relatorio
    extra = 1

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'inicio', 'local']
    list_filter = ['local', 'categorias']
    search_fields = ['titulo']
    inlines = [AtividadesInline, RelatorioInline]


