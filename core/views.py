from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login as auth_login
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from .decorators import group_required
from django.contrib import messages
from django.shortcuts import render
from django.core.paginator import *
from core.models import Product
from core.cart import Cart
from rest_framework import viewsets
from .serializers import *
from rest_framework.renderers import JSONRenderer
import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



from .models import *
from .forms import *
from .forms import LoginForm
from .models import Periodista
from .models import Product
from .models import Noticia
from .forms import NoticiaForm






def index(request):
    return render(request, 'core/index.html')
@login_required
def formulario(request):
    return render(request, 'core/formulario.html')
def detalle(request):
    return render(request, 'core/detalle.html')
def periodista(request):
    return render(request, 'core/periodista.html')
def vistaUser(request):
    return render(request, 'core/vistaUser.html')
def indexAdmin(request):
    return render(request, 'core/periodistas/indexAdmin.html')
def add(request):
    return render(request, 'core/periodistas/crud/add.html')
def update(request):
    return render(request, 'core/periodistas/crud/update.html')


def account_locked(request):
    return render(request, 'core/account_locked.html')


@login_required
def perfil(request):
    return render(request, 'core/perfil.html')
@login_required
def checkout(request):
    return render(request, 'core/checkout.html')

def login(request):
    return render(request, 'core/registration/login.html')

def register(request):
    aux ={
        'form':Customusercreation()
    }
    return render(request, 'core/registration/register.html',aux)


#=====================CRUD PERIODISTA=========================

def periodistas(request):
    periodistas = Periodista.objects.all()
    aux = {
        'lista': periodistas
    }
    return render(request, 'core/periodistas/indexAdmin.html', aux)




def add(request):
    aux = {
        'form' : PeriodistaForm()
    }
    
    if request.method == 'POST':
        formulario = PeriodistaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = 'Periodista agregado correctamente!'
        else:
            aux['form'] = formulario
            aux['msj'] = 'Error, no se pudo almacenar el empleado!'
    return render(request, 'core/periodistas/crud/add.html', aux)       


def update(request, id):
    periodista = Periodista.objects.get(id=id)
    aux = {
        'form' : PeriodistaForm(instance=periodista)
    }
    if request.method == 'POST':
        formulario = PeriodistaForm(data=request.POST, instance = periodista)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            aux['msj'] = 'Periodista modificado correctamente!'
        else:
            aux['form'] = formulario
            aux['msj'] = 'Error, no se pudo modificar!'
           
    return render(request, 'core/periodistas/crud/update.html', aux)



def periodistasdelete(request, id):
    periodista = Periodista.objects.get(id=id)
    periodista.delete()
    return redirect(to="indexAdmin")

#=====================FIN CRUD PERIODISTA=========================

def login_view(request):
    form = AuthenticationForm()
    return render(request, 'core/registration/login.html', {'form': form})

def register(request):
    msj = ''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            msj = 'Registro exitoso!'
           
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/registration/register.html', {'form': form, 'msj': msj})





#====================NOTICIA===========================

@group_required('Editor')
def confirmar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    noticia.estado = 'aceptada'
    noticia.save()
    return redirect('listanoticias')

def noticias_aceptadas(request):
    noticias_list = Noticia.objects.filter(estado='aceptada').order_by('-fecha')
    
    paginator = Paginator(noticias_list, 3) 
    page = request.GET.get('page')
    
    try:
        noticias = paginator.page(page)
    except PageNotAnInteger:
        noticias = paginator.page(1) 
    except EmptyPage:
        noticias = paginator.page(paginator.num_pages)
    
    return render(request, 'core/noticias_aceptadas.html', {'noticias': noticias})


@group_required('Periodistas')
@permission_required('core.add_noticia')
def procesar_noticia(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.usuario = request.user
            form.save()
            return redirect('noticias_usuarios')
    else:
        form = NoticiaForm()
    
    return render(request, 'formulario.html', {'form': form})

@group_required('Periodistas')
@permission_required('core.view_noticia')
def noticias_usuarios(request):
    noticias = Noticia.objects.filter(usuario=request.user)
    return render(request, 'noticiasUsuarios.html', {'noticias': noticias})


@group_required('Periodistas')
@permission_required('core.delete_noticia')
def borrar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    if request.method == 'POST':
        noticia.delete()
        return redirect('noticias_usuarios')
    return redirect('noticias_usuarios')

@group_required('Periodistas')
@permission_required('core.change_noticia')
def editar_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id) 
    
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('noticias_usuarios')
    else:
        form = NoticiaForm(instance=noticia)
    
    return render(request, 'core/formulario.html', {'form': form, 'noticia': noticia})

@group_required('Editor')
@permission_required('core.view_noticia')
def listanoticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'listanoticias.html', {'noticias': noticias})

@group_required('Editor')
@permission_required('core.change_noticia')
def cambiar_estado_noticia(request, noticia_id):
    noticia = get_object_or_404(Noticia, pk=noticia_id)
    
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')
        noticia.estado = nuevo_estado
        noticia.save()
        return redirect('listanoticias')
    
    return redirect('listanoticias')


#CART 

def cart_detail(request):
    cart = request.session.get(settings.CART_SESSION_ID, {})
    return render(request, 'core/cart/cart_detail.html', {'cart': cart})

def cart_add(request, id):
    product = Product.objects.get(id=id)  # Obtener el producto según el id
    cart = request.session.get(settings.CART_SESSION_ID, {})  # Obtener el carrito de la sesión
    if id in cart:
        cart[id]['quantity'] += 1
    else:
        cart[id] = {
            'id': product.id,
            'name': product.name,
            'image': product.image.url,
            'price': product.price,
            'quantity': 1
        }
        #guardamos el carrito de nuevo en la sesión
    request.session[settings.CART_SESSION_ID] = cart  
    return redirect('cart_detail') 

def item_increment(request, product_id):
    cart = request.session.get(settings.CART_SESSION_ID, {})
    if product_id in cart:
        cart[product_id]['quantity'] += 1
    request.session[settings.CART_SESSION_ID] = cart
    return redirect('cart_detail')

def item_decrement(request, product_id):
    cart = request.session.get(settings.CART_SESSION_ID, {})
    if product_id in cart and cart[product_id]['quantity'] > 1:
        cart[product_id]['quantity'] -= 1
    elif product_id in cart and cart[product_id]['quantity'] == 1:
        del cart[product_id]
    request.session[settings.CART_SESSION_ID] = cart
    return redirect('cart_detail')

def item_clear(request, product_id):
    cart = request.session.get(settings.CART_SESSION_ID, {})
    if product_id in cart:
        del cart[product_id]
    request.session[settings.CART_SESSION_ID] = cart
    return redirect('cart_detail')

def cart_clear(request):
    request.session[settings.CART_SESSION_ID] = {}
    return redirect('cart_detail')