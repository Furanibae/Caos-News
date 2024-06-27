from rest_framework import serializers
from .models import *




class TipoPeriodistaSerializers(serializers.ModelSerializer):
    class Meta:
        
        model = TipoPeriodista
        fields = '__all__'


class PeriodistaSerializers(serializers.ModelSerializer):
    tipo = TipoPeriodistaSerializers(read_only=True)
    class Meta:
        model = Periodista
        fields = '__all__'


