from django.urls import path
from . import views

app_name = 'devolucao'


urlpatterns = [
    path('devolver/', views.devolver, name="devolver"),
]