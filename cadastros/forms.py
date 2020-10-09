from django import forms

from cadastros.models import Cidade


class CidadeForm(forms.ModelForm):

    class Meta:
        model = Cidade
        # fields = ['nome', 'capital']
        fields = '__all__'