# Documentação de Seeds no Django

## O que é um Seed?

Um seed (semente) é um conjunto de dados iniciais que você quer inserir automaticamente no banco de dados. Em Django, isso é feito através de **Data Migrations**.

## Como Funciona

### 1. Data Migration Criada

Arquivo: `usuarios/migrations/0003_seed_usuario_inicial.py`

Esta migration cria automaticamente o usuário:
- **Email**: kilberty1995@gmail.com
- **Senha**: 1234 (armazenada com hash seguro)
- **Nome**: Kilberty
- **Permissões**: Superusuário com acesso ao admin

### 2. Executar a Migration

Para aplicar o seed, rode:

```bash
python manage.py migrate
```

A migration será executada automaticamente e o usuário será criado.

### 3. Verificar se foi Criado

```bash
python manage.py shell
```

No shell Python:

```python
from usuarios.models import Usuario

# Verificar se o usuário existe
usuario = Usuario.objects.get(email='kilberty1995@gmail.com')
print(f"Nome: {usuario.nome}")
print(f"Email: {usuario.email}")
print(f"É superusuário: {usuario.is_superuser}")
```

### 4. Fazer Login

Você pode fazer login com:
- **Email**: kilberty1995@gmail.com
- **Senha**: 1234

## Criar Novos Seeds

### Passo 1: Criar Migration Vazia

```bash
python manage.py makemigrations usuarios --empty --name seed_dados_iniciais
```

### Passo 2: Editar a Migration

```python
from django.db import migrations

def criar_dados(apps, schema_editor):
    """Função que cria os dados"""
    MinhaTabela = apps.get_model('app_name', 'MinhaTabela')
    
    # Criar registros
    MinhaTabela.objects.create(
        campo1='valor1',
        campo2='valor2',
    )

def remover_dados(apps, schema_editor):
    """Função para rollback (opcional)"""
    MinhaTabela = apps.get_model('app_name', 'MinhaTabela')
    MinhaTabela.objects.filter(campo1='valor1').delete()

class Migration(migrations.Migration):
    dependencies = [
        ('app_name', '0002_migration_anterior'),
    ]
    
    operations = [
        migrations.RunPython(criar_dados, remover_dados),
    ]
```

### Passo 3: Rodar a Migration

```bash
python manage.py migrate
```

## Boas Práticas

### ✅ Fazer

1. **Verificar se já existe** antes de criar:
   ```python
   if not Usuario.objects.filter(email='email@example.com').exists():
       Usuario.objects.create(...)
   ```

2. **Usar `make_password()`** para senhas:
   ```python
   from django.contrib.auth.hashers import make_password
   password=make_password('senha123')
   ```

3. **Criar função de rollback** para reverter:
   ```python
   migrations.RunPython(criar_dados, remover_dados)
   ```

4. **Usar `apps.get_model()`** em vez de importar diretamente:
   ```python
   Usuario = apps.get_model('usuarios', 'Usuario')
   ```

### ❌ Evitar

1. **Não importar modelos diretamente**:
   ```python
   # ❌ Errado
   from usuarios.models import Usuario
   
   # ✅ Correto
   Usuario = apps.get_model('usuarios', 'Usuario')
   ```

2. **Não usar senhas em texto plano**:
   ```python
   # ❌ Errado
   password='1234'
   
   # ✅ Correto
   password=make_password('1234')
   ```

3. **Não duplicar dados** - sempre verifique se já existe

## Exemplos Práticos

### Criar Múltiplos Usuários

```python
def criar_usuarios(apps, schema_editor):
    Usuario = apps.get_model('usuarios', 'Usuario')
    
    usuarios_iniciais = [
        {
            'email': 'admin@example.com',
            'password': make_password('admin123'),
            'nome': 'Administrador',
            'is_staff': True,
            'is_superuser': True,
        },
        {
            'email': 'user@example.com',
            'password': make_password('user123'),
            'nome': 'Usuário Normal',
            'is_staff': False,
            'is_superuser': False,
        },
    ]
    
    for dados_usuario in usuarios_iniciais:
        if not Usuario.objects.filter(email=dados_usuario['email']).exists():
            Usuario.objects.create(**dados_usuario)
```

### Criar Dados com Relacionamentos

```python
def criar_dados_relacionados(apps, schema_editor):
    Usuario = apps.get_model('usuarios', 'Usuario')
    Categoria = apps.get_model('app', 'Categoria')
    Produto = apps.get_model('app', 'Produto')
    
    # Criar usuário
    usuario = Usuario.objects.create(
        email='vendedor@example.com',
        password=make_password('123456'),
        nome='Vendedor',
    )
    
    # Criar categoria
    categoria = Categoria.objects.create(
        nome='Eletrônicos',
    )
    
    # Criar produto relacionado
    Produto.objects.create(
        nome='Notebook',
        categoria=categoria,
        usuario=usuario,
        preco=2500.00,
    )
```

### Seed com Bulk Create (Mais Eficiente)

```python
def criar_dados_bulk(apps, schema_editor):
    Produto = apps.get_model('app', 'Produto')
    
    produtos = [
        Produto(nome=f'Produto {i}', preco=i * 10)
        for i in range(1, 101)
    ]
    
    Produto.objects.bulk_create(produtos)
```

## Reverter Migration

Se precisar desfazer:

```bash
python manage.py migrate usuarios 0002_usuario_nome
```

Isso vai executar a função de rollback (`remover_usuario_inicial`) e deletar o usuário criado.

## Dicas

1. **Ambiente de Desenvolvimento**: Use seeds para dados de teste
2. **Ambiente de Produção**: Use seeds apenas para dados essenciais (usuário admin, configurações)
3. **Senhas Fortes**: Em produção, use senhas fortes e nunca commite senhas reais no código
4. **Variáveis de Ambiente**: Para produção, considere usar variáveis de ambiente:

```python
import os
from django.contrib.auth.hashers import make_password

def criar_admin(apps, schema_editor):
    Usuario = apps.get_model('usuarios', 'Usuario')
    
    admin_email = os.getenv('ADMIN_EMAIL', 'admin@example.com')
    admin_password = os.getenv('ADMIN_PASSWORD', 'changeme')
    
    if not Usuario.objects.filter(email=admin_email).exists():
        Usuario.objects.create(
            email=admin_email,
            password=make_password(admin_password),
            nome='Admin',
            is_superuser=True,
            is_staff=True,
        )
```

## Referências

- [Django Migrations Documentation](https://docs.djangoproject.com/en/stable/topics/migrations/)
- [Data Migrations](https://docs.djangoproject.com/en/stable/topics/migrations/#data-migrations)
