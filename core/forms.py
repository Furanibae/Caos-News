from django import forms
from django.forms import ModelForm
from .models import Periodista
from .models import *
from .views import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField
from django_recaptcha.fields import ReCaptchaField


class PeriodistaForm(ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Periodista
        #Pondremos qué campos queremos hacer visibles y que queremos modificar (ej1)
        #o podemos mostrarlos todos (ej2)
        #Ej1:
        #fields = ['rut', 'nombre','apellido']
        #Ej2:
        fields = '__all__'
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control form-control-sm mb-2', 'placeholder': 'Ingrese RUT'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control form-control-sm mb-2', 'placeholder': 'Ingrese nombre'}),
            'apellido' : forms.TextInput(attrs={'class': 'form-control form-control-sm mb-2', 'placeholder': 'Ingrese apellido'}),
            'edad' : forms.NumberInput(attrs={'class': 'form-control form-control-sm mb-2', 'placeholder': 'Ingrese edad'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control form-control-sm mb-2', 'placeholder': 'Ingrese dirección'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control form-control-sm mb-2', 'placeholder': 'Ingrese telefono'}),
            'habilitado': forms.CheckboxInput(attrs={'class': 'form-check-input mb-2 ml-2'}),
            'genero': forms.Select(attrs={'class': 'form-control form-control-sm mb-2'}), 
            'tipo' : forms.Select(attrs={'class': 'form-control form-control-sm mb-4'}),
        }        

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = [
            'titular',
            'subtitulo',
            'cuerpo',
            'nombre_redactor',
            'fecha',
            'archivo_adjunto',
            'categoria',
            'codigo'
        ]




class TipoPeriodista(ModelForm):
    class Meta: 
        model=TipoPeriodista
        fields = '__all__'

class LoginForm(forms.Form):
    username  = forms.CharField(label="usuario")
    password  = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    captcha = CaptchaField()
    
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']