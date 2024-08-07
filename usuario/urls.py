from django.urls import path
from views import Cadastrar, Atualizar, Login, Logout

app_name="usuario"

urlpatterns = [
    path('cadastro', Cadastrar.as_view(), name="cadastrar"),
    path('atualizar/', Atualizar.as_view(), name="atualizar"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
]
