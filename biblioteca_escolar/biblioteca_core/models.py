# biblioteca_core/models.py
from django.db import models
from django.urls import reverse

class Livro(models.Model):
    titulo = models.CharField(max_length=200, help_text="Título do livro")
    autor = models.CharField(max_length=150, help_text="Autor do livro")
    genero = models.CharField(max_length=100, help_text="Gênero")
    ano_publicacao = models.IntegerField(help_text="Ano de Publicação")
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    quantidade_disponivel = models.PositiveIntegerField(default=1, help_text="Quantidade em estoque")

    class Meta:
        ordering = ['titulo']

    def get_absolute_url(self):
        """Retorna a URL para acessar uma instância específica de um livro."""
        return reverse('livro-detail', args=[str(self.id)])

    def __str__(self):
        """String para representar o objeto do Model."""
        return self.titulo