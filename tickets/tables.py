import django_tables2 as tables

from tickets.models import Solicitacao


class SolicitacaoTable(tables.Table):

    actions = tables.TemplateColumn(template_name='tickets/actions.html')

    class Meta:
        model = Solicitacao
        fields = ('actions', 'id', 'categoria', 'nome', 'email', 'assunto', 'status', 'atendente', 'data_solicitacao', 'ultima_solicitacao')