from django import forms
from .models import Category,SubCategory,Marca, UnidadMedida,Producto
#form de la categoria
class CategoryForm(forms.ModelForm):
    
    class Meta:
       
        model = Category
        fields=['description','estado']
    
    
    description = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control form-control-user",'placeholder':"descripcion"}))
        
#form de la subcategoria
class SubCategoryForm(forms.ModelForm):
    
    class Meta:
       
        model = SubCategory
        fields=['categoria','description','estado']
        
    
    description= forms.CharField(widget=forms.TextInput(attrs={'class':"form-control form-control-user",'placeholder':"descripcion"}))
    categoria = forms.ModelChoiceField(Category.objects.filter(estado=True))
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['categoria'].empty_label =  "Seleccione Categoría"

# form de la MARCA
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields=['description','estado']
    
    
    description = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control form-control-user",'placeholder':"descripcion"}))


#form de la unidad de medida

class UMForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields=['description','estado']
    
    
    description = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control form-control-user",'placeholder':"descripcion"}))

#form producto
class ProductoForm(forms.ModelForm):
    
    class Meta:
       
        model = Producto
        fields=['codigo','codigo_barra','description','estado','precio','stock','last_buy','marca','subcategory','unidadMedida']
        exclude =['user_modifc','user',' created_at','updated_at']
    
    
    
    # description= forms.CharField(widget=forms.TextInput(attrs={'class':"form-control form-control-user",'placeholder':"descripcion"}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['last_buy'].widget.attrs['readonly']=True
        self.fields['stock'].widget.attrs['readonly']=True