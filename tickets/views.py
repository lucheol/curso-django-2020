from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View

from tickets.forms import NovaSolicitacaoForm
from tickets.models import Interacao, Solicitacao
from tickets.tables import SolicitacaoTable


class NovaSolicitacao(View):

    def get(self, request):

        form = NovaSolicitacaoForm

        return render(request, 'tickets/form.html', {'form': form})

    def post(self, request):

        form = NovaSolicitacaoForm(request.POST, request.FILES)

        if form.is_valid():

            obj = form.save(commit=True)
            obj.save()

            interacao = Interacao.objects.create(solicitacao=obj, tipo=Interacao.TIPO_STATUS_CHANGE, descricao='Solicitação aberta')
            interacao.send_mail_message()

            return redirect('cidades-list')

        return render(request, 'tickets/form.html', {'form': form})


class SolicitacaoView(View):

    def get(self, request):

        qs = Solicitacao.objects.all().order_by('id')

        table = SolicitacaoTable(qs)

        context = {
            'table': table
        }
        return render(request, 'tickets/lista_tickets.html', context)

    def post(self, request):

        id = request.POST.get('id')
        solicitacao = get_object_or_404(Solicitacao, pk=id)

        tipo = request.POST.get('tipo')
        if tipo == 'resposta':
            mensagem = request.POST.get('mensagem', '')
            solicitacao.registrar_resposta(request.user, mensagem)

        elif tipo == 'finalizar':
            motivo = request.POST.get('motivo', '')
            operacao = request.POST.get('operacao', '')
            if operacao == 'c':
                solicitacao.cancelar(request.user, motivo)
            else:
                solicitacao.finalizar(request.user, motivo)

        return redirect('lista-solicitacao-ticket')


class AssinarView(View):

    def get(self, request, id):

        solicitacao = get_object_or_404(Solicitacao, pk=id)

        solicitacao.registrar_atendente(request.user)

        return redirect('lista-solicitacao-ticket')


class DetalheTicketView(View):

    def get(self, request, id):

        solicitacao = get_object_or_404(Solicitacao, pk=id)

        return render(request, 'tickets/detalhe.html', {'obj': solicitacao} )

