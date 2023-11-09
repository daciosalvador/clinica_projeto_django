from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('registrar/', views.registerUser, name='register'),
    
    path('', views.homepage, name='home'),
    path('pacientes/<str:nome>/', views.pacientes, name='paciente'),
    path('lista_pacientes/', views.lista_paciente, name='lista-paciente'),

    path('atualizar_consulta/<str:pk>/', views.atualizar_consulta, name='att-consulta'),
    path('remover_consulta/<str:pk>/', views.remover_consulta, name='remover-consulta'),
    path('marcar_consulta/<str:nome>/', views.marcar_consulta, name='marcar-consulta'),

    path('cadastrar_paciente/', views.cadastrar_cliente, name='cadastrar-paciente'),
    path('atualizar_paciente/<str:nome>/', views.atualizar_cliente, name='att-paciente'),
]

