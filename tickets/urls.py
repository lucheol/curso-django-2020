from django.contrib.auth.decorators import login_required
from django.urls import include, path

from tickets.apis import SolicitacaoAPIView
from tickets.views import NovaSolicitacao

urlpatterns = [
    path('tickets/', NovaSolicitacao.as_view(), name='nova-solicitacao-ticket'),
    path('tickets/api', SolicitacaoAPIView.as_view(), name='solicitacao-api-ticket'),
]