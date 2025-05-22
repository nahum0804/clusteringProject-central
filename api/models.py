from django.db import models
import uuid

class Cliente(models.Model):
    id_cliente = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cedula = models.CharField(max_length=15, unique=True)
    nombre_completo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    saldo_actual = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Nodo(models.Model):
    ip_nodo = models.CharField(primary_key=True,max_length=100)
    name_nodo = models.CharField(max_length=100)
class HistorialEnvio(models.Model):
    id_envio = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)
    costo_envio = models.DecimalField(max_digits=10, decimal_places=2)
    qr_codigo = models.TextField()
    ip_nodo = models.ForeignKey(Nodo, on_delete=models.SET_NULL, null=True)

class HistorialPago(models.Model):
    id_pago = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    medio_pago = models.CharField(max_length=50)

