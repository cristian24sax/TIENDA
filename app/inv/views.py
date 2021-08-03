  
from django.shortcuts import  render, redirect
from django.contrib.auth.decorators import login_required,permission_required
from .form import CategoryForm,SubCategoryForm,MarcaForm,UMForm,ProductoForm
from .models import Category,SubCategory,Marca, UnidadMedida,Producto 
from django.contrib import messages
# Create your views here.

@login_required(login_url='login')
@permission_required('inv.view_category',login_url='SinPrivilegios')
def categoryview(request):
    categorias =Category.objects.all()
    return render(request,'inv/categoria_list.html',{
        
        'categorias':categorias
    
    })

@login_required(login_url='login')
def categoryNew(request):
    
    if request.method == 'POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('category')
    else:
        form =CategoryForm()
        return render(request,'inv/categoria_forms.html',{
        'category_form': form
        
    })
      
  
@login_required(login_url='login')
def deletecategory(request,id):
    category=Category.objects.get(pk=id)
    category.delete()

    return redirect('category')


@login_required(login_url='login')
def editarCategory(request,id):
    category=Category.objects.get(pk=id)

    if request.method =='POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')
    
    else:
        form = CategoryForm(instance=category)
        return render(request,'inv/categoria_forms.html',{'category_form':form,
        'categorias':category
        })

# views de sub categoria
@login_required(login_url='login')
@permission_required('inv.view_subcategory',login_url='SinPrivilegios')
def Subcategoryview(request):
    subcategorias =SubCategory.objects.all()
    return render(request,'inv/subcategoria_list.html',{
        
        'subcategorias':subcategorias
    
    })
            
@login_required(login_url='login')
def SubcategoryNew(request):
   
    if request.method == 'POST':
        form=SubCategoryForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('subcategory')
    else:
        form =SubCategoryForm()
        return render(request,'inv/subcategoria_forms.html',{
        'subcategory_form': form,
        
        
    })

def deleteSubcategory(request,id):
    subcategory=SubCategory.objects.get(pk=id)
    subcategory.delete()

    return redirect('subcategory')

def editarSubCategory(request,id):
    subcategory=SubCategory.objects.get(pk=id)

    if subcategory:
        if request.method =='POST':
            form = SubCategoryForm(request.POST,instance=subcategory)
            if form.is_valid():
                form.save()
                return redirect('subcategory')
    
        else:
            form = SubCategoryForm(instance=subcategory)
            return render(request,'inv/subcategoria_forms.html',{'subcategory_form':form,
            'subcategorias':subcategory
            })

# view de Marca 

@login_required(login_url='login')
@permission_required('inv.view_marca',login_url='SinPrivilegios')
def Marcaview(request):
    marcas =Marca.objects.all()
    return render(request,'inv/marca_list.html',{
        
        'marcas':marcas
    
    })
            
@login_required(login_url='login')
def MarcaNew(request):
   
    if request.method == 'POST':
        form=MarcaForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('marca_list')
    else:
        form =MarcaForm()
        return render(request,'inv/marca_forms.html',{
        'marca_form': form,
        
        
    })

def inactivarMarca(request,id):
    marca=Marca.objects.get(pk=id)
    marca.estado = False
    messages.success(request,'Marca inactivada')
    marca.save()
    return redirect('marca_list')

def ActivarMarca(request,id):
    marca=Marca.objects.get(pk=id)
    marca.estado = True
    marca.save()
    return redirect('marca_list')

def editarMarca(request,id):
    marca=Marca.objects.get(pk=id)
    if marca:
        if request.method =='POST':
            form = MarcaForm(request.POST,instance=marca)
            if form.is_valid():
                form.save()
                return redirect('marca_list')
    
        else:
            form =MarcaForm(instance=marca)
            return render(request,'inv/marca_forms.html',{'marca_form':form,
            'marcas':marca
            })

#views de Unidad de Medida   
@login_required(login_url='login')
@permission_required('inv.view_unidadMedida',login_url='SinPrivilegios')
def UMview(request):
    um =UnidadMedida.objects.all()
    return render(request,'inv/um_list.html',{
        
        'um':um
    
    })
@login_required(login_url='login')
def UMNew(request):
   
    if request.method == 'POST':
        form=UMForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('um_list')
    else:
        form =UMForm()
        return render(request,'inv/um_form.html',{
        'um_form': form,
        
        
    })

def inactivarUM(request,id):
    marca=UnidadMedida.objects.get(pk=id)
    marca.estado = False
    marca.save()
    return redirect('um_list')

def ActivarUM(request,id):
    marca=UnidadMedida.objects.get(pk=id)
    marca.estado = True
    marca.save()
    return redirect('um_list')

def editarUM(request,id):
    ums=UnidadMedida.objects.get(pk=id)
    if ums:
        if request.method =='POST':
            form = UMForm(request.POST,instance=ums)
            if form.is_valid():
                form.save()
                return redirect('um_list')
    
        else:
            form =UMForm(instance=ums)
            return render(request,'inv/um_form.html',{'um_form':form,
            'ums':ums
            })

#productos

@login_required(login_url='login')
def Productoview(request):
    productos =Producto.objects.all()
    return render(request,'inv/producto_list.html',{
        
        'productos':productos
    
    })
@login_required(login_url='login')
def ProductoNew(request):
   
    if request.method == 'POST':
        form=ProductoForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('producto_list')
    else:
        form =ProductoForm()
        return render(request,'inv/producto_form.html',{
        'producto_form': form,
        
        
    })

def inactivarProducto(request,id):
    marca=Producto.objects.get(pk=id)
    marca.estado = False
    marca.save()
    return redirect('producto_list')

def ActivarProducto(request,id):
    marca=Producto.objects.get(pk=id)
    marca.estado = True
    marca.save()
    return redirect('producto_list')

def editarProducto(request,id):
    producto=Producto.objects.get(pk=id)
    if producto:
        if request.method =='POST':
            form = ProductoForm(request.POST,instance=producto)
            if form.is_valid():
                form.save()
                return redirect('producto_list')
    
        else:
            form =ProductoForm(instance=producto)
            return render(request,'inv/producto_form.html',{
            'producto_form':form,
            'productos':producto,
           
            })
