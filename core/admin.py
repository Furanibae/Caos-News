from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin
from admin_confirm import AdminConfirmMixin
# Register your models here.

class TipoPeriodistaAdmin(AdminConfirmMixin,admin.ModelAdmin):
    confirm_change = True
    confirmation_fields = ['descripcion']

class PeriodistaModelAdmin(AdminConfirmMixin, admin.ModelAdmin):
    confirm_change = True
    confirmation_fields = ['rut', 'nombre','apellido','edad']


admin.site.register(Periodista,PeriodistaModelAdmin)
admin.site.register(TipoPeriodista,TipoPeriodistaAdmin)
admin.site.register(Noticia)
admin.site.register(Product)