from django.urls import path
from .import views 



urlpatterns = [

    path('client',views.Clienteview,name='cliente'),
    path('client_new',views.clienteNew,name='clienteNew'),
    path('editclient/<int:id>',views.editarCliente,name='editarCliente'),
    path('cliente/estado/<int:id>',views.clienteInactivar,name='Inactivar')
]