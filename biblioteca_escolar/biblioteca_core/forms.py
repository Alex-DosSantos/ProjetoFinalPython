from django import forms
from .models import Livro, Emprestimo

class LivroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Itera sobre todos os campos do formulário
        for field_name, field in self.fields.items():
            # Adiciona a classe 'form-control' do Bootstrap a cada campo
            field.widget.attrs['class'] = 'form-control'
            # Caso especial para o campo de upload de imagem para garantir a consistência
            if isinstance(field.widget, forms.FileInput):
                field.widget.attrs['class'] += ' form-control-file'
            # Caso especial para o campo de sinopse, para dar mais espaço
            if isinstance(field.widget, forms.Textarea):
                field.widget.attrs['rows'] = 4


    class Meta:
        model = Livro
        fields = '__all__' # Mantém todos os campos do modelo

class EmprestimoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Emprestimo
        fields = ['livro', 'aluno', 'data_devolucao_prevista']
        widgets = {
            'data_devolucao_prevista': forms.DateInput(attrs={'type': 'date'}),
        }