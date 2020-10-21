from rest_framework import serializers
from cadastros.models import Cidade, Estado


#https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
class CidadeSerializer(serializers.ModelSerializer):

    estado_nome = serializers.ReadOnlyField(source='estado.nome')
    # pais_nome = serializers.ReadOnlyField(source='estado.pais.nome')
    # estado = serializers.PrimaryKeyRelatedField(queryset=Estado.objects.all())

    class Meta:
        model = Cidade
        fields = ['id','estado', 'estado_nome', 'nome', 'capital', 'descricao']

class TestSerializer(serializers.Serializer):

    nome = serializers.CharField(max_length=45)
