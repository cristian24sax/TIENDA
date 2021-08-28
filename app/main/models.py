
# Create your models here.
from django.db import models
from django_userforeignkey.models.fields import UserForeignKey
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


class Class_Modelo2(models.Model):
    estado = models.BooleanField(default=True,verbose_name="Estado")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Creado el ")
    update_at = models.DateTimeField(auto_now=True,verbose_name="Actualizado el ")
    user = UserForeignKey(auto_user_add=True, related_name="+")
    user_modifc= UserForeignKey(auto_user_add=True,  related_name="+")
    class Meta:
        abstract=True