from django.db import models
from main.models import Class_Modelo
# Create your models here.
class Category(Class_Modelo):
    description = models.CharField(max_length=250,verbose_name="Descripcion",help_text = 'descripcion de la categoria',unique=True)
    class Meta:
        verbose_name ="Categoria"
        verbose_name_plural ="Categorias"

    def __str__(self):
        return self.description

class SubCategory(Class_Modelo):
    categoria=models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.CharField(max_length=250,verbose_name="Descripcion",help_text = 'descripcion de la categoria')

     

    class Meta:
        verbose_name ="Sub Categoria"
        verbose_name_plural ="Sub Categorias"
        unique_together = ('categoria','description')
    
    def __str__(self):
        return f" {self.categoria.description} , {self.description}" 


class Marca(Class_Modelo):
    description = models.CharField(max_length=100,help_text=" descripcion de la marca",unique=True,verbose_name="descripcion")
    title = models.CharField(max_length=50,blank=True)
    class Meta:
        verbose_name ="Marca"
        verbose_name_plural ="Marcas"
    def __str__(self):
        return self.description
    
class UnidadMedida(Class_Modelo):
    description = models.CharField(max_length=100,help_text=" descripcion de la Unidad de Medida",unique=True,verbose_name="descripcion")


    def __str__(self):
        return self.description

    class Meta:
        verbose_name ="Unidad de Medida"
        verbose_name_plural ="Unidades de Medidas"

class Producto(Class_Modelo):
    codigo=models.CharField(max_length=20,unique=True)
    description = models.CharField(max_length=200)
    codigo_barra=models.CharField(max_length=50)
    precio=models.FloatField(default=0)
    stock=models.IntegerField(default=0,null=True)
    last_buy=models.DateField(null=True,blank=True)

    marca=models.ForeignKey(Marca,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    unidadMedida=models.ForeignKey(UnidadMedida,on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    
    class Meta:
        verbose_name ="Producto"
        verbose_name_plural ="Productos"
        unique_together = ('codigo','codigo_barra')
    