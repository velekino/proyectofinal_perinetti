from pyexpat.errors import messages
from django.shortcuts import render
from http.client import HTTPResponse

from django.urls import is_valid_path

from miblogApp.models import *
from django.http import HttpResponse
from miblogApp.forms import Blogentradanueva, UsuarioRegistro

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

def verindex(request):
  
    return render(request, 'index.html')

def aboutme(request):
   
    return render(request, 'aboutme.html')

def blog(request):
   
    lista_blog= Blog.objects.all()
    context = {'lista_blog': lista_blog}
    
    #return render(request, 'index.html', context=context)   
    return render(request, 'blog.html', context=context)    
    
@login_required   
def curriculum(request):

    return render(request, 'curriculum.html')

def portfolio(request):
    
    return render(request, 'portfolio.html')

def contacto(request):
    
 
    if request.method=="POST":
    
               
                formularioentrada = Contacto(nombre=request.POST["nombre"],email=request.POST["email"],mensaje=request.POST["mensaje"])
            #    formularioentrada = Contacto(nombre=info["nombre"],email=info["email"],mensaje=info["mensaje"])
                formularioentrada.save()
               # return render(request, 'index.html' )
                
                return render(request,'index.html', f"Se ha guardado su mensaje!")
    else:

            formu1 = Contacto()
    return render(request, 'contacto.html', {"contacto":formu1})    





def blogentrada(request): 
    
    if request.method=="POST":
        formu1= Blogentradanueva(request.POST, request.FILES)
      
        if formu1.is_valid():
       
                info = formu1.cleaned_data 
               
           # vieja formularioentrada = Blog(titulo=request.POST["titulo"],tipo="2",imagen=request.POST["imagen"],texto=request.POST["texto"],fechapost=request.POST["fechapost"],autor="juanca" )
                formularioentrada = Blog(titulo=info["titulo"],tipo=info["tipo"],imagen=info["imagen"],texto=info["texto"],fechapost=info["fechapost"],autor=info["autor"] )
                formularioentrada.save()
                return render(request, 'index.html' )
    else:

            formu1 = Blogentradanueva()
    return render(request, 'formblogentrada.html', {"blogentrada":formu1})    

def buscaentrada(request):
    if request.GET["busqueda"]:
       busqueda = request.GET["busqueda"]
       entradas = Blog.objects.filter(texto__icontains=busqueda)
       
       return render(request, "blog.html", {"lista_blog":entradas})
    else:
        respuesta = "no enviaste datos." 
    return HttpResponse(respuesta)

def editarentrada(request, blogId):
     
    entrada = Blog.objects.get(id=blogId)
     
    if request.method=="POST":
        formu1= Blogentradanueva(request.POST, request.FILES)
      
        if formu1.is_valid():
       
                info = formu1.cleaned_data 

                entrada.titulo = info["titulo"]
                entrada.tipo =  info["tipo"]
                entrada.imagen = info["imagen"]
                entrada.texto = info["texto"]
                entrada.fechapost = info["fechapost"]
                entrada.autor = info["autor"]

                entrada.save()
               # vieja formularioentrada = Blog(titulo=request.POST["titulo"],tipo="2",imagen=request.POST["imagen"],texto=request.POST["texto"],fechapost=request.POST["fechapost"],autor="juanca" )
               # formularioentrada = Blog(titulo=info["titulo"],tipo=info["tipo"],imagen=info["imagen"],texto=info["texto"],fechapost=info["fechapost"],autor=info["autor"] )
               # formularioentrada.save()
                return render(request, 'index.html' )
    else:

            formu1 = Blogentradanueva(initial={"titulo":entrada.titulo,"tipo":entrada.tipo,"imagen":entrada.imagen,"texto":entrada.texto,"fechapost":entrada.fechapost,"autor":entrada.autor})
    return render(request, 'formblogentrada.html', {"blogentrada":formu1, "id":blogId}) 


@login_required 
def borrarentrada(request, blogId): 
    entrada = Blog.objects.get(id=blogId)
    entrada.delete()
    lista_blog= Blog.objects.all()
    context = {'lista_blog': lista_blog}
    
    #return render(request, 'index.html', context=context)   
    return render(request, 'blog.html', context=context) 

# Create your views here.


class ListarCv(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Cv
    template_name = "cv_list.html"

class DetalleCv(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Cv
    template_name = "cv_detail.html"

class CrearCv(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Cv
    template_name = "cv_form.html"
    success_url = "/curriculum/list"
    fields = ["tipo","ano","texto_cv","subtexto"]
    
class EditarCv(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Cv
    success_url = "/curriculum/list"
    template_name = "cv_form.html"
    fields = ["tipo","ano","texto_cv","subtexto"]

class BorrarCv(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Cv
    template_name = "cv_confirm_delete.html"
    success_url = "/curriculum/list"


#Portfolio~######

class ListarPortfolio(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Portfolio
    template_name = "portfolio_list.html"

class DetallePortfolio(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Portfolio
    template_name = "portfolio_detail.html"

class CrearPortfolio(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Portfolio
    template_name = "portfolio_form.html"
    success_url = "/portfolio/list"
    fields = ["titulo_portfolio","giturl","texto_portfolio"]
    
class EditarPortfolio(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Portfolio
    success_url = "/portfolio/list"
    template_name = "portfolio_form.html"
    fields = ["titulo_portfolio","giturl","texto_portfolio"]

class BorrarPortfolio(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Portfolio
    template_name = "portfolio_confirm_delete.html"
    success_url = "/portfolio/list"








def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username = usuario, password = contra)

            if user:
                login (request,user)

                return render(request, "index.html", {"mensaje":f"Bienvenido {user}"})
        else:

            return render (request, "index.html", {"mensaje": "Datos incorrectos."})

    else:
        
        form = AuthenticationForm()
    
    return render (request, "login.html", {"formulario":form})

def register_request(request):
    if request.method == "POST":
        form = UsuarioRegistro(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            
            form.save()
            return render(request, "index.html", {"mensaje":f"Usuario creado {username}."})
        else:

            return render (request, "index.html", {"mensaje": "Datos incorrectos."})

    else:
        
        form = UsuarioRegistro()
    
    return render (request, "registro.html", {"formulario":form})
    


        