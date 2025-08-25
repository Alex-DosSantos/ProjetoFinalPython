from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db import models, transaction
from .models import Livro, Emprestimo
from .forms import LivroForm, EmprestimoForm
from django.contrib.auth.models import User


def home(request):
    
    num_livros = Livro.objects.count()
    num_emprestimos_ativos = Emprestimo.objects.filter(status='ativo').count()
    num_usuarios = User.objects.count()
    
    
    livros_recentes = Livro.objects.order_by('-id')[:4]
    
    context = {
        'num_livros': num_livros,
        'num_emprestimos_ativos': num_emprestimos_ativos,
        'num_usuarios': num_usuarios,
        'livros_recentes': livros_recentes,
    }
    return render(request, 'biblioteca_core/home.html', context)


class LivroListView(LoginRequiredMixin, ListView):
    model = Livro
    template_name = 'biblioteca_core/livro_list.html'
    context_object_name = 'livros'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                models.Q(titulo__icontains=query) | models.Q(autor__icontains=query)
            )
        return queryset

class LivroDetailView(LoginRequiredMixin, DetailView):
    model = Livro
    template_name = 'biblioteca_core/livro_detail.html'

class LivroCreateView(LoginRequiredMixin, CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'biblioteca_core/livro_form.html'
    success_url = reverse_lazy('livro-list')

class LivroUpdateView(LoginRequiredMixin, UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = 'biblioteca_core/livro_form.html'
    success_url = reverse_lazy('livro-list')

class LivroDeleteView(LoginRequiredMixin, DeleteView):
    model = Livro
    template_name = 'biblioteca_core/livro_confirm_delete.html'
    success_url = reverse_lazy('livro-list')


class EmprestimoListView(LoginRequiredMixin, ListView):
    model = Emprestimo
    template_name = 'biblioteca_core/emprestimo_list.html'
    context_object_name = 'emprestimos'

class EmprestimoCreateView(LoginRequiredMixin, CreateView):
    model = Emprestimo
    form_class = EmprestimoForm
    template_name = 'biblioteca_core/emprestimo_form.html'
    success_url = reverse_lazy('emprestimo-list')

    def form_valid(self, form):
        emprestimo = form.save(commit=False)
        livro = emprestimo.livro
        
        with transaction.atomic():
            if livro.quantidade_disponivel > 0:
                livro.quantidade_disponivel -= 1
                livro.save()
                emprestimo.save()
                messages.success(self.request, f"Empréstimo do livro '{livro.titulo}' realizado com sucesso!")
                return super().form_valid(form)
            else:
                messages.error(self.request, f"Não há exemplares disponíveis do livro '{livro.titulo}' para empréstimo.")
                return self.form_invalid(form)