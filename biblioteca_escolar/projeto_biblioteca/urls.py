# projeto_biblioteca/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inclui as URLs do app biblioteca_core
    path('', include('biblioteca_core.urls')),
    # Inclui as URLs de autenticação padrão do Django (login, logout)
    path('contas/', include('django.contrib.auth.urls')),
]