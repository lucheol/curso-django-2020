from django.shortcuts import render, redirect
from django.views.generic.base import View

from tickets.forms import NovaSolicitacaoForm
from tickets.models import Interacao


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
