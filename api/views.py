from rest_framework import viewsets
from .models import Cliente, HistorialEnvio, HistorialPago
from .serializers import ClienteSerializer, HistorialEnvioSerializer, HistorialPagoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class HistorialEnvioViewSet(viewsets.ModelViewSet):
    queryset = HistorialEnvio.objects.all()
    serializer_class = HistorialEnvioSerializer

class HistorialPagoViewSet(viewsets.ModelViewSet):
    queryset = HistorialPago.objects.all()
    serializer_class = HistorialPagoSerializer