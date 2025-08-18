"""
URL configuration for projeto project.

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
from home import views
from mycontacts import views as mycontacts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('deletar/<int:id>/', views.deletar_usuario, name='deletar_usuario'),
    path('editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    
    # 14/08/2025 -> adicionar urls de "mycontacts"
    path('', mycontacts_views.mycontacts, name='mycontacts'),
    path('add/', mycontacts_views.adicionar),
    path('deletar_contact/<int:id>/', mycontacts_views.deletar_usuario, name='deletar_usuario_contact'),
    path('editarContato/<int:id>/', mycontacts_views.editarContato, name='editarContato'),
]

# models -> banco de dados
# views -> lógica (das urls)
# templates -> apresentação (html, css, js)
