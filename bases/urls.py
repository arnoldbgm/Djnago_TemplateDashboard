from django.urls import path
from .views import Home
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', auth_view.LoginView.as_view(template_name="bases/login.html"), name="login"),
    path('logout/', auth_view.LogoutView.as_view(), name="logout"),  # Eliminamos template_name aquí
]
