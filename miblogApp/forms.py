
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
class Blogentradanueva(forms.Form):
    
    titulo = forms.CharField()
    tipo = forms.IntegerField()
    imagen = forms.ImageField()
    texto = forms.CharField()
    fechapost = forms.DateField()
    autor=forms.CharField()

class UsuarioRegistro (UserCreationForm):
    email = forms.EmailField()
    
    password1: forms.CharField(label ="Contraseña", widget=forms.PasswordInput ) 
    
    password2: forms.CharField(label ="Repetir la Contraseña", widget=forms.PasswordInput ) 

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

class Contacto(forms.Form):
    
    nombre = forms.CharField()
    email = forms.EmailField()
    nombre = forms.Textarea()
   
