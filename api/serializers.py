from rest_framework import serializers
from .models import Cliente, HistorialEnvio, HistorialPago,Nodo

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class HistorialEnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialEnvio
        fields = '__all__'

class HistorialPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialPago
        fields = '__all__'

class NodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nodo
        fields = '__all__'