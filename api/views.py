from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Cliente, HistorialEnvio, HistorialPago, Nodo
from .serializers import ClienteSerializer, HistorialEnvioSerializer, HistorialPagoSerializer, NodoSerializer
from rest_framework.views import APIView

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    @action(detail=False, methods=["post"], url_path="bulk_sync")
    def bulksync(self, request):
        data = request.data
        resultados = []
        for item in data:
            try:
                obj,  = self.queryset.model.objects.update_or_create(
                    defaults=item,
                    **{self.queryset.model._meta.pk.name: item[self.queryset.model._meta.pk.name]}
                )
                resultados.append(str(obj.pk))
            except Exception as e:
                continue
        return Response({"status": "ok", "procesados": len(resultados)})

class HistorialEnvioViewSet(viewsets.ModelViewSet):
    queryset = HistorialEnvio.objects.all()
    serializer_class = HistorialEnvioSerializer
    @action(detail=False, methods=["post"], url_path="bulk_sync")
    def bulksync(self, request):
        data = request.data
        resultados = []
        for item in data:
            try:
                obj,  = self.queryset.model.objects.update_or_create(
                    defaults=item,
                    **{self.queryset.model._meta.pk.name: item[self.queryset.model._meta.pk.name]}
                )
                resultados.append(str(obj.pk))
            except Exception as e:
                continue
        return Response({"status": "ok", "procesados": len(resultados)})

class HistorialPagoViewSet(viewsets.ModelViewSet):
    queryset = HistorialPago.objects.all()
    serializer_class = HistorialPagoSerializer
    @action(detail=False, methods=["post"], url_path="bulk_sync")
    def bulksync(self, request):
        data = request.data
        resultados = []
        for item in data:
            try:
                obj,  = self.queryset.model.objects.update_or_create(
                    defaults=item,
                    **{self.queryset.model._meta.pk.name: item[self.queryset.model._meta.pk.name]}
                )
                resultados.append(str(obj.pk))
            except Exception as e:
                continue
        return Response({"status": "ok", "procesados": len(resultados)})


class NodoViewSet(viewsets.ModelViewSet):
    queryset = Nodo.objects.all()
    serializer_class = NodoSerializer
    @action(detail=False, methods=["post"], url_path="bulk_sync")
    def bulksync(self, request):
        data = request.data
        resultados = []
        for item in data:
            try:
                obj,  = self.queryset.model.objects.update_or_create(
                    defaults=item,
                    **{self.queryset.model._meta.pk.name: item[self.queryset.model._meta.pk.name]}
                )
                resultados.append(str(obj.pk))
            except Exception as e:
                continue
        return Response({"status": "ok", "procesados": len(resultados)})

class ConsultaQRView(APIView):
    def get(self, request, qr_codigo):
        try:
            envio = HistorialEnvio.objects.get(qr_codigo=qr_codigo)
            serializer = HistorialEnvioSerializer(envio)
            return Response(serializer.data)
        except HistorialEnvio.DoesNotExist:
            return Response({"error": "Código QR no encontrado"}, status=status.HTTP_404_NOT_FOUND)
    
        
class HistorialGeneralEnviosView(ListAPIView):
    queryset = HistorialEnvio.objects.all().order_by('-fecha_envio')
    serializer_class = HistorialEnvioSerializer
    
