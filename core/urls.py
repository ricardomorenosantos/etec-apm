"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from financeiro.views import saldo
from django.conf import settings
from django.conf.urls.static import static
from core.views import home
from documentos.views import listar_atas
from documentos.views import listar_atas, listar_termos
from patrimonio.views import listar_patrimonios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saldo/', saldo),
    path('', home),
    path('atas/', listar_atas, name='listar_atas'),
    path('termos/', listar_termos, name='listar_termos'),
    path('patrimonios/', listar_patrimonios),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)