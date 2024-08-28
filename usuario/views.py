from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from utils.geradorMatricula import gerar_matricula

from .models import Usuario
from . import forms

class BasePerfil(View):
    template_name = 'usuario/cadastro.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.perfil = None

        if self.request.user.is_authenticated:
            self.perfil = Usuario.objects.filter(
                usuario=self.request.user
            ).first()

            self.contexto = {
                'userform': forms.UserForm(
                    data = self.request.POST or None,
                    usuario = self.request.user,
                    instance = self.request.user,
                ),
                'perfilform': forms.PerfilForm(
                    data = self.request.POST or None,
                    instance = self.perfil,
                )
            }
        else:
            self.contexto = {
                'userform': forms.UserForm(
                    data = self.request.POST or None
                ),
                'perfilform': forms.PerfilForm(
                    data = self.request.POST or None
                )
            }

        self.userform = self.contexto['userform']
        self.perfilform = self.contexto['perfilform']

        if self.request.user.is_authenticated:
            self.template_name = 'usuario/atualizar.html'
        
        self.renderizar = render(
            self.request, 
            self.template_name, 
            self.contexto
        )

    def get(self,*args, **kwargs):
        return self.renderizar  
    
class Cadastrar(BasePerfil):
    def post(self, *args, **kwargs):
        if not self.userform.is_valid() or not self.perfilform.is_valid():
            messages.error(
                self.request,
                'Verifique se todos os campos foram preenchidos corretamente.'
            )
            return self.renderizar
        
        username = self.userform.cleaned_data.get('username')
        password = self.userform.cleaned_data.get('password')
        email = self.userform.cleaned_data.get('email')
        first_name = self.userform.cleaned_data.get('first_name')
        last_name = self.userform.cleaned_data.get('last_name')

        telefone = self.perfilform.cleaned_data.get('telefone')
        data_nascimento = self.perfilform.cleaned_data.get('data_nascimento')
        
        if self.request.user.is_authenticated:
            usuario = get_object_or_404(
                User, 
                username=self.request.user.username
            )
            usuario.username = username
            
            if password:
                usuario.set_password(password)

            usuario.email = email
            usuario.first_name = first_name
            usuario.last_name = last_name
            usuario.save()


            if not self.perfil:
                perfil = Usuario(
                    nome=f"{first_name} {last_name}",
                    email=email,
                    telefone=telefone,
                    matricula=gerar_matricula(),
                    data_nascimento=data_nascimento
                )
                perfil.save()
            else:
                self.perfil.nome = f"{first_name} {last_name}"
                self.perfil.email = email
                self.perfil.telefone = telefone
                self.perfil.data_nascimento = data_nascimento
                perfil.save()

        else:
            usuario = self.userform.save(commit=False)
            usuario.set_password(password)
            usuario.save()

            perfil = Usuario(
                usuario=usuario,
                nome=f"{first_name} {last_name}",
                email=email,
                telefone=telefone,
                matricula=gerar_matricula(),
                data_nascimento=data_nascimento
            )
            perfil.save()

        if password:
            autentica = authenticate(
                self.request,
                username=usuario,
                password=password
            )
            if autentica:
                login(self.request, 
                      user=usuario
                )
        
        self.request.session.save()

        messages.success(
            self.request,
            'Login realizado com sucesso!'
        )

        return redirect('livro:home')

class Atualizar(View):
    ...

class UserLogin(View):
    template_name = 'usuario/login.html'
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            print('Login realizado com sucesso!')
            return redirect('livro:home')
        else:
            messages.error(request, 'Nome de usuário ou senha incorretos.')
            print('Login ou senha incorretos.')
            return render(request, self.template_name)
        
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Logout(View):
    def get(self, *args, **kwargs):
        logout(self.request)
        self.request.session.save()
        return redirect('usuario:login')