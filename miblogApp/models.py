from django.db import models

# Create your models here.
class Verindex(models.Model):
    #modelo de las entradas del blog que se muestran en el index, la idea es forzar la herencia de esta clase para el blog, y asi poder usar verindex para mostrar el blog en el index
     #no es un bug es un feature :P
    titulo = models.CharField(max_length=60)
    tipo = models.IntegerField()
    #quitar tipo
    imagen = models.ImageField(upload_to ='uploads/')
    texto = models.CharField(max_length=600)
    fechapost = models.DateField()
    autor=models.CharField(max_length=10)

#class aboutme(models.Model):
    #modelo del parrafo de about
#    pass

class Cv(models.Model):
    #esta clase modela entradas de bd, cada entrada se compila en mi cv.
    tipo=models.IntegerField()
    ano=models.IntegerField()
    texto_cv= models.CharField(max_length=60)
    subtexto= models.TextField()


class Portfolio(models.Model):
    
    titulo_portfolio=models.CharField(max_length=100)
    
    giturl= models.URLField( max_length=200)
    texto_portfolio=models.CharField(max_length=200)

class Blog(Verindex):
    
    class Meta:
        proxy = True
    #testing herencia proxy

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    mensaje = models.TextField()