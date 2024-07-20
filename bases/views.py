# views.py
from django.shortcuts import render
from django.views import generic
# Este mixin va actuar como un midleware el cual exigira que este logeando antes de que pueda ver la vista
from django.contrib.auth.mixins import LoginRequiredMixin
class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    # Si no esta registrado mi usario le dire que se vaya al ..
    login_url='bases:login'
