from rest_framework import permissions
from rest_framework.generics import ListAPIView

from tickets.models import Solicitacao
from tickets.serializers import SolicitacaoSerializer


class SolicitacaoAPIView(ListAPIView):
    queryset = Solicitacao.objects.all()
    serializer_class = SolicitacaoSerializer
    permission_classes = [permissions.IsAuthenticated]