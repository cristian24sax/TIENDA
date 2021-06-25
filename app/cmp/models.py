from django.db import models
from main.models import Class_Modelo
# Create your models here.

class Proveedor(Class_Modelo):
    description = models.CharField(max_length=100,unique=True,verbose_name="descripcion")
    direction=  models.CharField(max_length=250,null=True,blank=True,verbose_name="direccion")
    contact= models.CharField(max_length=100,verbose_name="Contacto")
    phone= models.CharField(max_length=10,null=True,blank=True,verbose_name="Telefono")
    email= models.CharField(max_length=250,null=True,blank=True,verbose_name="Email")

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural ='Proveedores'

    def __str__(self):
        return self.description