from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import copy

from . import models
from . import forms

class BasePerfil(View):
    template_name = 'usuario/cadastro.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.perfil = None

        if self.request.user.is_authenticated:
            self.perfil = models.Usuario.objects.filter(
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
                    instance = self.request.user,
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

            self.perfilform.cleaned_data['email'] = email
            self.perfilform.cleaned_data['nome'] = f"{first_name} {last_name}"

            if not self.perfil:
                self.perfilform.cleaned_data['usuario'] = usuario
                perfil = models.Perfil(**self.perfilform.cleaned_data)
                perfil.save()
            else:
                perfil = self.perfilform.save(commit=False)
                perfil.usuario = usuario
                perfil.save()

        else:
            usuario = self.userform.save(commit=False)
            usuario.set_password(password)
            usuario.save()

            self.perfilform.cleaned_data['email'] = email
            self.perfilform.cleaned_data['nome'] = f"{first_name} {last_name}"

            perfil = self.perfilform.save(commit=False)
            perfil.usuario = usuario
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

class Login(View):
    def post(self, *args, **kwargs):
        form = forms.PerfilForm(self.request.POST)

        if not form.is_valid():
            messages.error(
                self.request,
                'Usuário e/ou senha inválidos'
            )
            return redirect('usuario:cadastro')
        
        username = form.cleaned_data.get('matricula')
        password = form.cleaned_data.get('password')

        usuario = authenticate(
            self.request, username=username, password=password)
        
        if not usuario:
            messages.error(
                self.request,
                'Usuário e/ou senha inválidos'
            )
            return redirect('usuario:cadastro')

        login(self.request, user=usuario)

        messages.success(
            self.request,
            'Login realizado com sucesso!'
        )
        
        return redirect('livro:home')

class Logout(View):
    def get(self, *args, **kwargs):
        logout(self.request)
        self.request.session.save()
        return redirect('usuario:cadastro')