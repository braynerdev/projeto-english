from django import forms
from .models import Palavras


class CadastroModelForm(forms.ModelForm):
    class Meta:
        model = Palavras
        fields = ['palavra', 'traducao']
        