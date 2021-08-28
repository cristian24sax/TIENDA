from django.shortcuts import render,redirect,HttpResponse
from .models import Cliente
from  .forms import ClienteForm
from django.contrib import messages
# Create your views here.
def Clienteview(request):
    Clientes =Cliente.objects.all()
    return render(request,'fac/clientes_list.html',{
        
        'obj':Clientes
    
    })

def clienteNew(request):
    if request.method == 'POST':
        form=ClienteForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            success_message="Registro Agregado Satisfactoriamente"
            return redirect('cliente')
    else:
        form =ClienteForm()
        return render(request,'fac/cliente_form.html',{
        'cliente_form': form,
        
        
    })


def editarCliente(request,id):
    cliente=Cliente.objects.get(pk=id)
    if cliente:
        if request.method =='POST':
            form = ClienteForm(request.POST,instance=cliente)
            if form.is_valid():
                form.save()
                return redirect('cliente')
    
        else:
            form =ClienteForm(instance=cliente)
            return render(request,'fac/cliente_form.html',{
            'cliente_form':form,
            'obj':cliente,
           
            })

def clienteInactivar(request,id):
    cliente=Cliente.objects.filter(pk=id).first()

    if request.method =='POST':
        if cliente:
            cliente.estado=not cliente.estado
            cliente.save()
            return HttpResponse('OK')
        
        
    
    return HttpResponse('Fail')
