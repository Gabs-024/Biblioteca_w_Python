from django.urls import path
from .views import Cadastrar, Atualizar, UserLogin, Logout

app_name="usuario"

urlpatterns = [
    path('', UserLogin.as_view(), name="login"),
    path('cadastrar/', Cadastrar.as_view(), name="cadastrar"),
    path('atualizar/', Atualizar.as_view(), name="atualizar"),
    path('logout/', Logout.as_view(), name="logout"),
]
