from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import *
from rest_framework import routers
from .views import *
from . import views



urlpatterns = [
    path('', index, name="index"),
    path('detalle/', detalle, name="detalle"),
    path('formulario/', formulario, name="formulario"),
    path('periodista/', periodista, name="periodista"),
    path('vistaUser/', vistaUser, name="vistaUser"),
    path('periodistas/', views.periodistas, name="indexAdmin"),
    path('periodistas/crud/add/',add, name="add"),
    path('periodistas/crud/update/<id>', update, name="update"),
    path('periodistas/crud/delete/<id>', periodistasdelete, name="periodistasdelete"),
    path('registration/login/', login, name='login'),
    path('registration/register/',register, name="register"),
    path('checkout/',checkout, name="checkout"),
    #noticia


    path('procesar_noticia/', views.procesar_noticia, name='procesar_noticia'),
    path('noticias_usuarios/', views.noticias_usuarios, name='noticias_usuarios'),
    path('borrar-noticia/<int:noticia_id>/', views.borrar_noticia, name='borrar_noticia'),
    path('editar_noticia/<int:noticia_id>/', views.editar_noticia, name='editar_noticia'),
    path('listanoticias/', views.listanoticias, name='listanoticias'),
    path('cambiar_estado/<int:noticia_id>/', views.cambiar_estado_noticia, name='cambiar_estado_noticia'),
    path('confirmar_noticia/<int:noticia_id>/', views.confirmar_noticia, name='confirmar_noticia'),
    path('noticias_aceptadas/', views.noticias_aceptadas, name='noticias_aceptadas'),
    
    
    #API
    #path('api/', include(router.urls)),

    #account locked
    path('account_locked/',account_locked, name="account_locked"),

    #CART
     path('cart/add/<int:id>/', views.cart_add, name='cart_add'),    
     path('cart/detail/', views.cart_detail, name='cart_detail'),
     path('cart/item_increment/<int:product_id>/', views.item_increment, name='item_increment'),
     path('cart/item_decrement/<int:product_id>/', views.item_decrement, name='item_decrement'),
     path('cart/item_clear/<int:product_id>/', views.item_clear, name='item_clear'),

]



