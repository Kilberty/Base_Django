from inertia import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login,logout
import json
from django.http.response import JsonResponse
from .forms import UsuarioForm
from .models import Usuario

def index(request):
    usuario_logado = request.user
    
    # Pega os parâmetros de filtro da URL (query params)
    # Exemplo: /usuarios/?nome=João&email=joao@email.com
    filtro_nome = request.GET.get('nome', '').strip()
    # Adicione mais filtros conforme necessário:
    # filtro_email = request.GET.get('email', '').strip()
    # filtro_status = request.GET.get('status', '').strip()
    
    # Inicia a query base
    usuarios = Usuario.objects.all()
    
    # Aplica os filtros se eles existirem
    if filtro_nome:
        # icontains = case insensitive contains (busca parcial, ignora maiúsculas/minúsculas)
        usuarios = usuarios.filter(nome__icontains=filtro_nome)
    
    # Exemplo de como adicionar mais filtros:
    # if filtro_email:
    #     usuarios = usuarios.filter(email__icontains=filtro_email)
    # if filtro_status:
    #     usuarios = usuarios.filter(status=filtro_status)
    
    # Ordena e seleciona apenas os campos necessários
    usuarios = usuarios.values('id', 'nome', 'email').order_by('id')
    
    props = {
        "usuario": {
            "id": usuario_logado.id if usuario_logado.is_authenticated else None,
            "nome": getattr(usuario_logado, "nome", ""),
            "email": getattr(usuario_logado, "email", "")
        },
        "usuarios_cadastrados": list(usuarios)
    }
    return render(request, "Usuarios", props)


@csrf_exempt
def usuario_login(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('UTF-8'))
        email = data.get('email')
        senha = data.get('password')
        print(email,senha)
        
        user = authenticate(request,email=email,password=senha)
        if user is not None:
            login(request, user)
            return render(request, "Usuarios", {})
        else:
            return render(request, "Login", {"errors": {"email": ["Usuário ou senha incorretos"]}})

    return render(request, "Login", {})


@login_required
def usuario_logout(request):
    if request.method == "POST":
       logout(request)
       return render(request,"Login",{})
    return render(request,"Login",{})

@csrf_exempt
def cadastro(request):
    if request.method == "POST":
       data = json.loads(request.body.decode('UTF-8'))
       form = UsuarioForm(data)
       if form.is_valid():
           user = form.save(commit=False)
           user.set_password(form.cleaned_data["password"])
           user.save()
           usuarios = Usuario.objects.filter().values('id', 'nome', 'email').order_by('id')
           props = {
                 "usuarios_cadastrados": list(usuarios)
            }
           
           return render(request, "Usuarios", props)
   
       else:
           # Retornar resposta Inertia completa com status 422 e os erros
           usuario_logado = request.user
           usuarios = Usuario.objects.filter().values('id', 'nome', 'email').order_by('id')
           props = {
               "usuario": {
                   "id": usuario_logado.id if usuario_logado.is_authenticated else None,
                   "nome": getattr(usuario_logado, "nome", ""),
                   "email": getattr(usuario_logado, "email", "")
               },
               "usuarios_cadastrados": list(usuarios),
               "errors": form.errors
           }
           response = render(request, "Usuarios", props)
           response.status_code = 422
           return response
    
    # Se não for POST, redireciona para a página de usuários
    from django.shortcuts import redirect
    return redirect('usuarios:index')   
       
       
       
       