from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db import models, transaction
from django.utils import timezone
from .models import Livro, Emprestimo
from .forms import LivroForm, EmprestimoForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """ Garante que o usuário logado seja um membro da equipe (staff). """
    def test_func(self):
        return self.request.user.is_staff


class RegistroView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        messages.success(self.request, "Conta criada com sucesso! Agora você pode fazer o login.")
        return super().form_valid(form)


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
            queryset = queryset.filter(models.Q(titulo__icontains=query) | models.Q(autor__icontains=query))
        return queryset
class LivroDetailView(LoginRequiredMixin, DetailView):
    model = Livro
    template_name = 'biblioteca_core/livro_detail.html'


class LivroCreateView(StaffRequiredMixin, CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'biblioteca_core/livro_form.html'
    success_url = reverse_lazy('livro-list')
class LivroUpdateView(StaffRequiredMixin, UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = 'biblioteca_core/livro_form.html'
    success_url = reverse_lazy('livro-list')
class LivroDeleteView(StaffRequiredMixin, DeleteView):
    model = Livro
    template_name = 'biblioteca_core/livro_confirm_delete.html'
    success_url = reverse_lazy('livro-list')


class EmprestimoListView(LoginRequiredMixin, ListView):
    model = Emprestimo
    template_name = 'biblioteca_core/emprestimo_list.html'
    context_object_name = 'emprestimos'


class EmprestimoCreateView(StaffRequiredMixin, CreateView):
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
class EmprestimoPendenteListView(LoginRequiredMixin, ListView):
    model = Emprestimo
    template_name = 'biblioteca_core/emprestimos_pendentes.html'
    context_object_name = 'emprestimos'
    def get_queryset(self):
        return Emprestimo.objects.filter(status='ativo').order_by('data_devolucao_prevista')


@user_passes_test(lambda u: u.is_staff)
@require_POST
def devolver_livro(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    with transaction.atomic():
        if emprestimo.status == 'ativo':
            emprestimo.status = 'devolvido'
            emprestimo.data_devolucao_real = timezone.now().date()
            emprestimo.save()
            livro = emprestimo.livro
            livro.quantidade_disponivel += 1
            livro.save()
            messages.success(request, f"O livro '{livro.titulo}' foi marcado como devolvido com sucesso!")
        else:
            messages.warning(request, "Este empréstimo já foi finalizado.")
    return redirect('emprestimo-list')