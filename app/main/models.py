from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Class_Modelo(models.Model):
    estado = models.BooleanField(default=True,verbose_name="Estado")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Creado el ")
    update_at = models.DateTimeField(auto_now=True,verbose_name="Actualizado el ")
    user = models.ForeignKey(User,editable=False,verbose_name="Usuario",on_delete=models.CASCADE)
    user_modifc=models.IntegerField(blank=True,null=True)
    class Meta:
        abstract=True