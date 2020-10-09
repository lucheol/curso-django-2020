from django.urls import include, path

from cadastros.views import lista_cidades, detalhe_cidade

urlpatterns = [
    path('', lista_cidades, name='cidades-list'),
    path('detail/<int:id>/', detalhe_cidade, name='cidades-detalhe')
]