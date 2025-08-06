# biblioteca_core/views.py
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Livro
from .forms import LivroForm

def home(request):
    return render(request, 'biblioteca_core/home.html')

class LivroListView(LoginRequiredMixin, ListView):
    model = Livro
    template_name = 'biblioteca_core/livro_list.html'
    context_object_name = 'livros'

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