from django.urls import path
from .import views 
from.views import CompraDetDelete
from .reportes import reporte_compras,imprimir_compra

urlpatterns = [
    path('proveedor/',views.proveedorview,name='proveedor'),
    path('proveedorNew/',views.proveedorNew,name='proveedorNew'),
    path('editarProveedor/<int:id>',views.editarProveedor,name='editarProveedor'),
    path('deleteProveedor/<int:id>',views.deleteProveedor,name='delete'),
    path('inactivarProveedor/<int:id>',views.inactivarProveedor,name='inactivarProveedor'),

    #compras 
    path('compras/',views.Comprasview,name='compras_list'),
    path('compras/new',views.compras,name='comprasNew'),
    path('compras/edit/<int:compra_id>',views.compras,name='compras_edit'),
    path('compras/<int:compra_id>/delete/<int:pk>',CompraDetDelete.as_view(),name='compras_del'),
    #html2pdf
    path('compras/listado',reporte_compras,name='compras_print_all'),
    path('compras/<int:compra_id>/imprimir',imprimir_compra,name='compras_print_one')
]