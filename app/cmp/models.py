from django.db import models
from main.models import Class_Modelo

from inv.models import Producto
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

class ComprasEnc(Class_Modelo):
    fecha_compra=models.DateField(null=True,blank=True)
    observacion=models.TextField(blank=True,null=True)
    no_factura=models.CharField(max_length=100)
    fecha_factura=models.DateField()
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)

    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.observacion)

    def save(self):
        self.observacion = self.observacion.upper()
        if self.sub_total == None  or self.descuento == None:
            self.sub_total = 0
            self.descuento = 0
            
        self.total = self.sub_total - self.descuento
        super(ComprasEnc,self).save()

    class Meta:
        verbose_name_plural = "Encabezado Compras"
        verbose_name="Encabezado Compra"

class ComprasDet(Class_Modelo):
    compra=models.ForeignKey(ComprasEnc,on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad=models.BigIntegerField(default=0)
    precio_prv=models.FloatField(default=0)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)
    costo=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self):
        self.sub_total = float(float(int(self.cantidad)) * float(self.precio_prv))
        self.total = self.sub_total - float(self.descuento)
        super(ComprasDet, self).save()
    
    class Meta:
        verbose_name_plural = "Detalles Compras"
        verbose_name="Detalle Compra"
