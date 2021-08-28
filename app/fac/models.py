from django.db import models
from main.models import Class_Modelo,Class_Modelo2
from inv.models import Producto
# Create your models here.

class Cliente(Class_Modelo):
    NAT='Natural'
    JUR='Juridica'
    Tipo_Cliente=[
        (NAT,'Natural'),
        (JUR,'Juridica')
    ]
    nombres = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    celular=models.CharField(max_length=20,null=True,blank=True)
    tipo=models.CharField(max_length=10, choices=Tipo_Cliente,default=NAT)

    def __str__(self):
        return self.apellido + " " + self.nombres

    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes' 


   
class FacturaEnc(Class_Modelo2):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.id)

    def save(self):
        self.total = self.sub_total - self.descuento
        super(FacturaEnc,self).save()

    class Meta:
        verbose_name_plural = "Encabezado Facturas"
        verbose_name="Encabezado Factura"
        permissions = [
            ('sup_caja_facturaenc','Permisos de Supervisor de Caja Encabezado')
        ]
    

class FacturaDet(Class_Modelo2):
    factura = models.ForeignKey(FacturaEnc,on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad=models.BigIntegerField(default=0)
    precio=models.FloatField(default=0)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self):
        self.sub_total = float(float(int(self.cantidad)) * float(self.precio))
        self.total = self.sub_total - float(self.descuento)
        super(FacturaDet, self).save()
    
    class Meta:
        verbose_name_plural = "Detalles Facturas"
        verbose_name="Detalle Factura"
        permissions = [
            ('sup_caja_facturadet','Permisos de Supervisor de Caja Detalle')
        ]
