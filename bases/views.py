# views.py
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Aquí vamos a crear nuestra vista


class Home(generic.TemplateView):
    # Con usar template_name va a renderizar la plantilla
    #  template_name = 'base/base.html'
    # Ahora que cree mi home le dire que me redireccione a donde a mi home.html
    template_name = 'bases/home.html'
