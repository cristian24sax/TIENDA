from django import forms

from .models import Proveedor

class ProveedorForm(forms.ModelForm):
  
    
    class Meta:
       
        model = Proveedor
        exclude =['user_modifc','user',' created_at','updated_at']
        
    
    email= forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control form-control-user"}))
    
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })