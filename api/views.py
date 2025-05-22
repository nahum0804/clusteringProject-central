from rest_framework import viewsets
from .models import Cliente, HistorialEnvio, HistorialPago, Nodo
from .serializers import ClienteSerializer, HistorialEnvioSerializer, HistorialPagoSerializer, NodoSerializer
from rest_framework.views import APIView


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class HistorialEnvioViewSet(viewsets.ModelViewSet):
    queryset = HistorialEnvio.objects.all()
    serializer_class = HistorialEnvioSerializer

class HistorialPagoViewSet(viewsets.ModelViewSet):
    queryset = HistorialPago.objects.all()
    serializer_class = HistorialPagoSerializer

class NodoViewSet(viewsets.ModelViewSet):
    queryset = Nodo.objects.all()
    serializer_class = NodoSerializer

class ConsultaQRView(APIView):
    def get(self, request, qr_codigo):
        try:
            envio = HistorialEnvio.objects.get(qr_codigo=qr_codigo)
            serializer = HistorialEnvioSerializer(envio)
            return Response(serializer.data)
        except HistorialEnvio.DoesNotExist:
            return Response({"error": "Código QR no encontrado"}, status=status.HTTP_404_NOT_FOUND)