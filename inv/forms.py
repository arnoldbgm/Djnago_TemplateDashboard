from django import forms
from .models import CatgoriaModel

# Para crear un formulario empezamos usando una clase

class CategoriaForm(forms.ModelForm):
   class Meta:
      model = CatgoriaModel
      fields = ['descripcion', 'estado']
      labels = {'descripcion': 'Descripcion de categoria',
                 'estado': 'Estado'}
      widget = {'descripcion': forms.TextInput}

   def __init__(self, *args, **kwargs):
      super().__init__(*args,**kwargs)
      for field in iter(self.fields):
         self.fields[field].widget.attrs.update({
            'class': 'form-control'
         })