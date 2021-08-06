from django.urls import path
from .import views

urlpatterns = [
    path('proveedor/',views.proveedorview,name='proveedor'),
    path('proveedorNew/',views.proveedorNew,name='proveedorNew'),
    path('editarProveedor/<int:id>',views.editarProveedor,name='editarProveedor'),
    path('deleteProveedor/<int:id>',views.deleteProveedor,name='delete'),
    path('inactivarProveedor/<int:id>',views.inactivarProveedor,name='inactivarProveedor'),
    
]