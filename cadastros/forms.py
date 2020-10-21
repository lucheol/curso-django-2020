from django import forms
from django.core.exceptions import ValidationError

from cadastros.models import Cidade

class TestForm(forms.Form):

    nome = forms.CharField(max_length=45, required=True)

class CidadeForm(forms.ModelForm):

    class Meta:
        model = Cidade
        # fields = ['nome', 'capital']
        fields = '__all__'

    def clean(self):

        nome = self.cleaned_data['nome']

        if nome == 'Itajubá':
            raise ValidationError({'nome': 'Não podemos cadastrar a cidade de Itajubá no sistema.'})