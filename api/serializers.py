from rest_framework import serializers
from .models import Cliente, HistorialEnvio, HistorialPago,Nodo

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

from rest_framework import serializers
from .models import HistorialEnvio, Nodo
import uuid

class HistorialEnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialEnvio
        fields = '__all__'
        read_only_fields = ['qr_codigo']

    def validate_ip_nodo(self, value):
        if not Nodo.objects.filter(ip_nodo=value.ip_nodo).exists():
            raise serializers.ValidationError("El nodo especificado no está registrado.")
        return value

    def create(self, validated_data):
        envio = HistorialEnvio.objects.create(**validated_data)

        qr_id = str(uuid.uuid4())
        envio.qr_codigo = qr_id
        envio.save()

        return envio


class HistorialPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialPago
        fields = '__all__'

class NodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nodo
        fields = '__all__'