from django import forms
from django.contrib.auth.models import User
from .models import Usuario

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        exclude = ('usuario', 'nome', 'email', 'matricula')

class UserForm(forms.ModelForm):
    password = forms.CharField(
        required = False,
        widget = forms.PasswordInput(),
        label = 'Senha',
    )
    password2 = forms.CharField(
    required = False,
    widget = forms.PasswordInput(),
    label = 'Confirmação de senha',
    )

    def __init__(self, *args, **kwargs):
        self.usuario = kwargs.pop('usuario', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('first_name',
                   'last_name',
                    'username',
                    'password',
                    'password2',
                    'email')
    
    def clean (self, *args, **kwargs):
        cleaned = super().clean()
        validation_error_msgs = {}

        usuario_data = cleaned.get('username')
        email_data = cleaned.get('email')
        password_data = cleaned.get('password')
        password2_data = cleaned.get('password2')

        usuario_db = User.objects.filter(username=usuario_data).first()
        email_db = User.objects.filter(email=email_data).first()

        error_msg_user_exists = 'Usuário já cadastrado'
        error_msg_email_exists = 'Email já cadastrado'
        error_msg_password_match = 'As senhas não são iguais'
        error_msg_password_short = 'Sua senha precisa ter no mínimo 8 caracteres'
        error_msg_required_field = 'Este campo é obrigatório'

        if self.usuario:
            if usuario_db:
                if usuario_data != usuario_db.username:
                    validation_error_msgs['username'] = error_msg_user_exists

            if email_db:
                if email_data != email_db.email:
                    validation_error_msgs['email'] = error_msg_email_exists

            if password_data:
                if password_data != password2_data:
                    validation_error_msgs['password'] = error_msg_password_match
                    validation_error_msgs['password2'] = error_msg_password_match
                if len(password_data) < 8:
                    validation_error_msgs['password'] = error_msg_password_short
        else:
            if usuario_db:
                validation_error_msgs['username'] = error_msg_user_exists

            if email_db:
                validation_error_msgs['email'] = error_msg_email_exists

            if not password_data:
                validation_error_msgs['password'] = error_msg_required_field

            if not password2_data:
                validation_error_msgs['password2'] = error_msg_required_field

            if password_data != password2_data:
                validation_error_msgs['password'] = error_msg_password_match
                validation_error_msgs['password2'] = error_msg_password_match

            if len(password_data) < 8:
                validation_error_msgs['password'] = error_msg_password_short

        if validation_error_msgs:
            raise(forms.ValidationError(validation_error_msgs))
        
        return cleaned
        