from django.urls import path
from .views import Home

# Ahora hare un login usando el LoginView que es propio de django
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', auth_view.LoginView.as_view(template_name="bases/login.html"), name="login")
]
