from rest_framework import serializers

from tickets.models import Solicitacao, Interacao


class InteracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interacao
        fields = '__all__'

class SolicitacaoSerializer(serializers.ModelSerializer):

    interacoes = InteracaoSerializer(many=True, read_only=True)

    class Meta:
        model = Solicitacao
        fields = ['id', 'categoria','nome', 'email', 'assunto', 'descricao', 'arquivo','status', 'atendente', 'data_solicitacao',
                  'ultima_atualizacao', 'interacoes']
