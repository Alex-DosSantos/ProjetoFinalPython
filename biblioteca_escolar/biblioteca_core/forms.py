# biblioteca_core/forms.py
from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__' # Inclui todos os campos do modelo no formulário