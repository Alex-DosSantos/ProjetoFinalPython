# biblioteca_core/models.py
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Livro(models.Model):
    titulo = models.CharField(max_length=200, help_text="Título do livro")
    autor = models.CharField(max_length=150, help_text="Autor do livro")
    sinopse = models.TextField(null=True, blank=True, help_text="Breve resumo do livro")
    genero = models.CharField(max_length=100, help_text="Gênero")
    ano_publicacao = models.IntegerField(help_text="Ano de Publicação")
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    quantidade_disponivel = models.PositiveIntegerField(default=1, help_text="Quantidade em estoque")
    capa = models.ImageField(upload_to='capas/', null=True, blank=True, help_text="Capa do livro")

    class Meta:
        ordering = ['titulo']

    def get_absolute_url(self):
        """Retorna a URL para acessar uma instância específica de um livro."""
        return reverse('livro-detail', args=[str(self.id)])

    def __str__(self):
        """String para representar o objeto do Model."""
        return self.titulo

class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('devolvido', 'Devolvido'),
    ]
    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, help_text="Livro a ser emprestado")
    aluno = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Aluno que realizou o empréstimo")
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao_prevista = models.DateField(help_text="Data prevista para devolução")
    data_devolucao_real = models.DateField(null=True, blank=True, help_text="Data em que o livro foi devolvido")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativo')

    class Meta:
        ordering = ['-data_emprestimo']

    def __str__(self):
        return f"{self.livro.titulo} emprestado para {self.aluno.username}"