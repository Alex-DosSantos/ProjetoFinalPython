from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from biblioteca_core.views import RegistroView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('biblioteca_core.urls')),
    
   
    path('contas/', include([
        
        path('', include('django.contrib.auth.urls')),
        
        path('registrar/', RegistroView.as_view(), name='register'),
    ])),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)