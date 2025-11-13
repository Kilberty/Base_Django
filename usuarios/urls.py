from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='listagem_usuario'),
    path('cadastrar/',views.cadastro,name='cadastro'),
    path('login/',views.usuario_login,name='autenticar'),
    path('logout/',views.usuario_logout,name='deslogar')
    
]
