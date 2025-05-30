"""
URL configuration for backend_cliente project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ClienteViewSet, HistorialEnvioViewSet, HistorialPagoViewSet, NodoViewSet, ConsultaQRView, HistorialGeneralEnviosView

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'historial_envios', HistorialEnvioViewSet)
router.register(r'historial_pagos', HistorialPagoViewSet)
router.register(r'nodos', NodoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/consulta_qr/<str:qr_codigo>/', ConsultaQRView.as_view(), name='consulta_qr'),
    path('api/historial_general_envios/', HistorialGeneralEnviosView.as_view(), name='historial_general_envios'),
]