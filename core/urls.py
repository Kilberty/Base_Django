from django.contrib import admin
from django.urls import path,include
from . import views
from usuarios import views as usuarios
urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/',include('usuarios.urls')),
    path('home/',views.home,name='home'),
    path('',usuarios.usuario_login,name='login')
    
]
