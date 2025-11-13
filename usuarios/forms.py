from django import forms
from django.contrib.auth import get_user_model

Usuario = get_user_model()


class UsuarioForm(forms.ModelForm):
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirmar Senha",
        error_messages={'required': 'Por favor, confirme a senha.'}
    )
    
    class Meta:
        model = Usuario
        fields = ["email", "nome", "password"]
        error_messages = {
            'email': {
                'required': 'O campo e-mail é obrigatório.',
                'invalid': 'Insira um e-mail válido.',
                'unique': 'Este e-mail já está cadastrado.',
            },
            'nome': {
                'required': 'O campo nome é obrigatório.',
            },
            'password': {
                'required': 'O campo senha é obrigatório.',
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("password")
        senha2 = cleaned_data.get("password2")
        
        if senha and senha2 and senha != senha2:
            raise forms.ValidationError("As senhas não coincidem.")
        
        return cleaned_data
