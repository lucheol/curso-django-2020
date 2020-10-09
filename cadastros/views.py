from django.shortcuts import render, get_object_or_404, redirect

from cadastros.forms import CidadeForm
from cadastros.models import Cidade


def lista_cidades(request):

    qs = Cidade.objects.all().order_by('nome')

    context = {
        'cidades': qs,
        'titulo': 'SIDIA'
    }

    return render(request, 'cadastros/lista_cidades.html', context)

def detalhe_cidade(request, id):

    # id_cidade = request.GET['id_cidade']

    # cidade = Cidade.objects.get(pk=id_cidade)
    cidade = get_object_or_404(Cidade, pk=id)

    context = {
        'cidade': cidade,
    }

    return render(request, 'cadastros/detalhe_cidades.html', context)

def remove_cidade(request, id):

    cidade = get_object_or_404(Cidade, pk=id)

    cidade.delete()

    return redirect('cidades-list')


def cadastra_cidade(request):

    if request.method == 'POST':

        form = CidadeForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('cidades-list')

        # nome = request.POST['nome']
        # capital = request.POST['capital']
        # Cidade.objects.create(nome=nome, capital=capital)

    else:
        form = CidadeForm()


    context = {
        'form': form
    }

    return render(request, 'cadastros/cadastra_cidades.html', context)