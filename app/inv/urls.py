from django.urls import path
from . import views

urlpatterns = [
    #categoria
    path('category/',views.categoryview,name='category'),
    path('CategoryNew/',views.categoryNew,name='categoryNew'),
    path('editar/<int:id>',views.editarCategory,name='editarCategoria'),
    path('delete/<int:id>',views.deletecategory,name='delete'),
    #subcategoria
    path('subcategory/',views.Subcategoryview,name='subcategory'),
    path('subCategoryNew/',views.SubcategoryNew,name='subcategoryNew'),
    path('editarsub/<int:id>',views.editarSubCategory,name='editarSubCategoria'),
    path('deletesub/<int:id>',views.deleteSubcategory,name='deleteSub'),

    #marca
    path('marca/',views.Marcaview,name='marca_list'),
    path('marcaNew/',views.MarcaNew,name='marcaNew'),
    path('editarMarca/<int:id>',views.editarMarca,name='editarMarca'),
    path('inactivarMarca/<int:id>',views.inactivarMarca,name='inactivarMarca'),
    path('ActivarMarca/<int:id>',views.ActivarMarca,name='ActivarMarca'),

    #unidad de medida
    path('unidad/',views.UMview,name='um_list'),
    path('umNew/',views.UMNew,name='UMNew'),
    path('editarUm/<int:id>',views.editarUM,name='editarUM'),
    path('inactivarUm/<int:id>',views.inactivarUM,name='inactivarUM'),
    path('ActivarUm/<int:id>',views.ActivarUM,name='ActivarUM'),

    #producto 
    path('producto/',views.Productoview,name='producto_list'),
    path('ProductoNew/',views.ProductoNew,name='ProductoNew'),
    path('editarProducto/<int:id>',views.editarProducto,name='editarProducto'),
    path('inactivarProducto/<int:id>',views.inactivarProducto,name='inactivarProducto'),
    path('ActivarProducto/<int:id>',views.ActivarProducto,name='ActivarProducto'),

]