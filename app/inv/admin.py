from django.contrib import admin
from .models import  Category,SubCategory,Category,Marca,UnidadMedida,Producto
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('user','created_at')
    list_display=('description','created_at')
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id= request.user.id

        obj.save()

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('stock','last_buy')
  

admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory)
admin.site.register(Marca)
admin.site.register(UnidadMedida)
admin.site.register(Producto,ProductoAdmin)



    