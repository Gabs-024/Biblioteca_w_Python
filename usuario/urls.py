from django.urls import path
from .views import Cadastrar, Atualizar, user_login, Logout

app_name="usuario"

urlpatterns = [
    path('', Cadastrar.as_view(), name="cadastro"),
    path('atualizar/', Atualizar.as_view(), name="atualizar"),
    path('login/', user_login, name="login"),
    path('logout/', Logout.as_view(), name="logout"),
]
