from django.db import models
from django.contrib.auth.models import User
import datetime
from django.conf import settings



class TipoPeriodista(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class Periodista(models.Model):

    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    
    TIPO_CHOICES = [
        ('periodista', 'Periodista'),
    ]  

    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    #EDAD: siempre dejar un valor o dejar los paréntesis vacíos
    #JAMAS sin paréntesis
    edad = models.IntegerField()
    direccion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=12)
    habilitado = models.BooleanField(default=True)
    #GENERO: el primer valor es el que ocupamos para trabajar y el segundo es visible en pantalla
    #[('datoquesetrabaja', 'Valorvisibleparalosusers')]
    genero = models.CharField(max_length=10, choices=[('masculino', 'Masculino'),('femenino','Femenino')], default='masculino')
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    tipo = models.ForeignKey(TipoPeriodista, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.rut




class Noticia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titular = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    nombre_redactor = models.CharField(max_length=50)
    fecha = models.DateField()
    archivo_adjunto = models.FileField(upload_to='noticias_archivos/', default='media/noticias_archivos/limon.jpg')
    categoria = models.CharField(max_length=50)
    codigo = models.CharField(max_length=20)
    estado = models.CharField(max_length=20, default='pendiente')

    def __str__(self):
        return f"{self.usuario.username} - {self.titular}"
    
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cart/products/', default='mensual.png')
    price = models.FloatField()

    def __str__(self):
        return self.name