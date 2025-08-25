from django.urls import path
from .views import (
    home,
    LivroListView,
    LivroDetailView,
    LivroCreateView,
    LivroUpdateView,
    LivroDeleteView,
    EmprestimoListView,
    EmprestimoCreateView,
)

urlpatterns = [
    # URL da Home
    path('', home, name='home'),
    
    # URLs de Livro
    path('livros/', LivroListView.as_view(), name='livro-list'),
    path('livro/<int:pk>/', LivroDetailView.as_view(), name='livro-detail'),
    path('livro/novo/', LivroCreateView.as_view(), name='livro-create'),
    path('livro/<int:pk>/editar/', LivroUpdateView.as_view(), name='livro-update'),
    path('livro/<int:pk>/deletar/', LivroDeleteView.as_view(), name='livro-delete'),
    
    # URLs de Empréstimo
    path('emprestimos/', EmprestimoListView.as_view(), name='emprestimo-list'),
    path('emprestimo/novo/', EmprestimoCreateView.as_view(), name='emprestimo-create'),
]