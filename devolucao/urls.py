from django.urls import path
from . import views

urlpatterns = [
    path('devolucao/', views.devolucao, name="devolucao"),
]