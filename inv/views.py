from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

# Ahora vamos a importar el formulario que creamos
from .models import CatgoriaModel
from .forms import CategoriaForm


# Recuerda que usamos el ListView para que muestra las tablas
class CategoriaView(LoginRequiredMixin, generic.ListView):
   model= CatgoriaModel
   template_name = "inv/categoria_list.html"

   # Recuerda que por defecto Django pone el nombre de obj al context
   context_object_name = "obj"
   login_url = "bases:login"


class CategoriaNew(LoginRequiredMixin, generic.CreateView):
   model=CatgoriaModel
   template_name="inv/categoria_form.html"
   context_object_name = "obj"
   form_class=CategoriaForm
   success_url=reverse_lazy("inv:categoria_list")
   login_url = "bases:login"

   # Cuando la data sea valida se guardara en la bd
   def form_valid(self, form):
      form.instance.user_creacion = self.request.user
      return super().form_valid(form)