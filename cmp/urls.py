from django.urls import path
from .views import ProveedorView

urlpatterns = [

    path('proveedor/', ProveedorView.as_view(), name='proveedor_list'),
    
]