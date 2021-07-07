from django.shortcuts import render,redirect,HttpResponse
from .models import Proveedor
from .forms import ProveedorForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def proveedorview(request):
    proveedores =Proveedor.objects.all()
    return render(request,'cmp/proveedor_list.html',{
        
        'proveedores':proveedores
    
    })

@login_required(login_url='login')
def proveedorNew(request):
    if request.method == 'POST':
        form=ProveedorForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('proveedor')
    else:
        form =ProveedorForm()
        return render(request,'cmp/proveedor_form.html',{
        'proveedor_form': form,
        
        
    })
      
  

def deleteProveedor(request,id):
    proveedor=Proveedor.objects.get(pk=id)
    proveedor.delete()

    return redirect('proveedor')

def editarProveedor(request,id):
    producto=Proveedor.objects.get(pk=id)
    if producto:
        if request.method =='POST':
            form = ProveedorForm(request.POST,instance=producto)
            if form.is_valid():
                form.save()
                return redirect('proveedor')
    
        else:
            form =ProveedorForm(instance=producto)
            return render(request,'cmp/proveedor_form.html',{
            'proveedor_form':form,
            'proveedores':producto,
           
            })


def inactivarProveedor(request,id):
    proveedor=Proveedor.objects.filter(pk=id).first()
    contexto={}
    template='cmp/inactivar_prv.html'
    if not proveedor:
        return HttpResponse('Proveedor no existe'+ str(id))

    if request.method=='GET':
        contexto={'proveedor':proveedor}
    
    if request.method=='POST':
        proveedor.estado = False
        proveedor.save()
        contexto={'proveedor':'OK'}
        return HttpResponse('Proveedor Inactivado')
        

    return render(request,template,contexto)
 
   