from django.contrib import admin

from tickets.models import Categoria, Solicitacao, Interacao


class InteracaoInline(admin.StackedInline):

    model = Interacao

class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'categoria', 'nome', 'email', 'assunto', 'status', 'atendente', 'data_solicitacao', 'ultima_atualizacao')
    list_filter = ('categoria', 'status', 'data_solicitacao', 'ultima_atualizacao')
    search_fields = ('nome', 'email', 'assunto')
    inlines = [
        InteracaoInline,
    ]

admin.site.register(Categoria)
admin.site.register(Solicitacao, SolicitacaoAdmin)
