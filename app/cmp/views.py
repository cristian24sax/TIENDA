from django.shortcuts import render,redirect,HttpResponse
from .models import Proveedor,ComprasDet,ComprasEnc
from .forms import ProveedorForm,ComprasEncForm
from inv.models import Producto
from django.contrib.auth.decorators import login_required,permission_required
import datetime
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
    template_name='cmp/inactivar_prv.html'
    contexto={}
    prv = Proveedor.objects.filter(pk=id).first()

    if not prv:
        return HttpResponse('Proveedor no existe ' + str(id))

    if request.method=='GET':
        contexto={'obj':prv}

    if request.method=='POST':
        prv.estado=False
        prv.save()
        contexto={'obj':'OK'}
        return HttpResponse('Proveedor Inactivado')

    return render(request,template_name,contexto)

# vistas de compras 
@login_required(login_url='login')
@permission_required('cmp.view_comprasenc',login_url='SinPrivilegios')
def Comprasview(request):
    comprasenc =ComprasEnc.objects.all()
    return render(request,'cmp/compras_list.html',{
        
        'compras':comprasenc
    
    })

@login_required(login_url='login')
@permission_required('cmp.view_comprasenc',login_url='SinPrivilegios')

def compras(request,compra_id=None):
    template_name='cmp/compras.html'
    prod=Producto.objects.filter(estado=True)
    form_compras={}
    contexto={}

    if request.method=='GET':
        form_compras=ComprasEncForm()
        enc = ComprasEnc.objects.filter(pk=compra_id).first()

        if enc:
            det = ComprasDet.objects.filter(compra=enc)
            fecha_compra = datetime.date.isoformat(enc.fecha_compra)
            fecha_factura = datetime.date.isoformat(enc.fecha_factura)
            e = {
                'fecha_compra':fecha_compra,
                'proveedor': enc.proveedor,
                'observacion': enc.observacion,
                'no_factura': enc.no_factura,
                'fecha_factura': fecha_factura,
                'sub_total': enc.sub_total,
                'descuento': enc.descuento,
                'total':enc.total
            }
            form_compras = ComprasEncForm(e)
        else:
            det=None
        
        contexto={'productos':prod,'encabezado':enc,'detalle':det,'form_enc':form_compras}
    
    return render(request,template_name,contexto)