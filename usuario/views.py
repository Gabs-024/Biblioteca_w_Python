from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import copy

from . import models
from . import forms

class BasePerfil(View):
    template_name = 'usuario/criar.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.carrinho = copy.deepcopy(self.request.session.get('carrinho'))

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
        
        nome = self.userform.cleaned_data.get('nome')
        matricula = self.userform.cleaned_data.get('matricula')
        email = self.userform.cleaned_data.get('email')
        telefone = self.userform.cleaned_data.get('telefone')
        senha = self.userform.cleaned_data.get('senha')
        confirma_senha = self.userform.cleaned_data.get('confirma_senha')
        
        if self.request.user.is_authenticated:
            usuario = get_object_or_404(
                User, 
                nome=self.request.user.nome
            )
            usuario.nome = nome
            
            if senha:
                usuario.set_senha(senha)

            usuario.email = email
            usuario.matricula = matricula
            usuario.telefone = telefone
            usuario.senha = senha
            usuario.confirma_senha = confirma_senha

            usuario.save()

            if not self.perfil:
                self.perfilform.cleaned_data['usuario'] = usuario
                perfil = models.Usuario(**self.perfilform.cleaned_data)
                perfil.save()
            else:
                perfil = self.perfilform.save(commit=False)
                perfil.usuario = usuario
                perfil.save()

        else:
            usuario = self.userform.save(commit=False)
            usuario.set_senha(senha)
            usuario.save()

            perfil = self.perfilform.save(commit=False)
            perfil.usuario = usuario
            perfil.save()

        if senha:
            autentica = authenticate(
                self.request,
                nome=usuario,
                senha=senha
            )
            if autentica:
                login(self.request, 
                    user=usuario
                )
        
        # self.request.session['carrinho'] = self.carrinho
        self.request.session.save()

        messages.success(
            self.request,
            'Login realizado com sucesso!'
        )

        return redirect('lista:livros')

class Atualizar(View):
    ...

class Login(View):
    def post(self, *args, **kwargs):
        nome = self.request.POST.get('nome')
        senha = self.request.POST.get('senha')

        if not nome or not senha:
            messages.error(
                self.request,
                'Usuário e/ou senha inválidos'
            )
            return redirect('usuario:cadastro')
        
        usuario = authenticate(
            self.request, nome=nome, senha=senha)
        
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
        
        return redirect('lista:livros')

class Logout(View):
    def get(self, *args, **kwargs):
        lista = copy.deepcopy(self.request.session.get('lista'))
        logout(self.request)
        self.request.session['lista'] = lista
        self.request.session.save()
        return redirect('lista:livros')