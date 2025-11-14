from django.db import migrations
from django.contrib.auth.hashers import make_password


def criar_usuario_inicial(apps, schema_editor):
    """Cria o usuário inicial kilberty1995@gmail.com"""
    Usuario = apps.get_model('usuarios', 'Usuario')
    
    # Verifica se o usuário já existe para evitar duplicação
    if not Usuario.objects.filter(email='kilberty1995@gmail.com').exists():
        Usuario.objects.create(
            email='kilberty1995@gmail.com',
            password=make_password('1234'),  # Hash seguro da senha
            nome='Kilberty',
            is_staff=True,  # Acesso ao admin
            is_superuser=True,  # Superusuário
            is_active=True,
        )


def remover_usuario_inicial(apps, schema_editor):
    """Remove o usuário inicial (rollback)"""
    Usuario = apps.get_model('usuarios', 'Usuario')
    Usuario.objects.filter(email='kilberty1995@gmail.com').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_nome'),
    ]

    operations = [
        migrations.RunPython(criar_usuario_inicial, remover_usuario_inicial),
    ]
