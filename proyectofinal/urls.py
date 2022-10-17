"""proyectofinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from re import template
from django.contrib import admin
from django.urls import path
from miblogApp.views import *
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
urlpatterns = [
    path('', verindex, name="index"),
    path('admin/', admin.site.urls),
    path('index/', verindex, name="index"),
    path('aboutme/', aboutme, name="aboutme"),
    path('blog/', blog, name="blog"),
    path('login/', LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('registro/', register_request, name="registro"),

    path('portfolio/', portfolio, name="portfolio"),
    path('contacto/', contacto, name="contacto"),
    
    path('blogentrada/', blogentrada, name="blogentrada"),
    path('buscaentrada/', buscaentrada, name="buscaentrada"),
    path('editarentrada/<blogId>', editarentrada, name="editarentrada"),
    path('borrarentrada/<blogId>', borrarentrada, name="borrarentrada"),
   
    path('curriculum/list', ListarCv.as_view(), name="curriculum"),
    path('editarcurriculum/<int:pk>', EditarCv.as_view(), name="editarcurriculum"),
    path('borrarcurriculum/<int:pk>', BorrarCv.as_view(), name="borrarcurriculum"),
    path('crearcurriculum/nuevo', CrearCv.as_view(), name="crearcurriculum"),
    path('detallecurriculum/<int:pk>', DetalleCv.as_view(), name="detallecurriculum"),

    path('portfolio/list', ListarPortfolio.as_view(), name="portfolio"),
    path('editarportfolio/<int:pk>', EditarPortfolio.as_view(), name="editarportfolio"),
    path('borrarportfolio/<int:pk>', BorrarPortfolio.as_view(), name="borrarportfolio"),
    path('crearportfolio/nuevo', CrearPortfolio.as_view(), name="crearportfolio"),
    path('detalleportfolio/<int:pk>', DetallePortfolio.as_view(), name="detalleportfolio"),




   
   
]
