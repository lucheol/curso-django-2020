from django.contrib.auth.decorators import login_required
from django.urls import include, path

from tickets.apis import SolicitacaoAPIView
from tickets.views import NovaSolicitacao, SolicitacaoView, AssinarView, DetalheTicketView

urlpatterns = [
    path('tickets/', login_required(SolicitacaoView.as_view()), name='lista-solicitacao-ticket'),
    path('tickets/novo', NovaSolicitacao.as_view(), name='nova-solicitacao-ticket'),
    path('tickets/api', SolicitacaoAPIView.as_view(), name='solicitacao-api-ticket'),
    path('tickets/assinar/<id>/', login_required(AssinarView.as_view()), name='assinar-solicitacao-ticket'),
    path('tickets/detalhe/<id>/', login_required(DetalheTicketView.as_view()), name='detalhe-solicitacao-ticket'),
]