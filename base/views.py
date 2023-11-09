from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout


from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .form import ConsultaForm, PacienteForm, PacienteAttForm, CriarUsuario

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, "Username ou password incorreto")

        context = {}

        return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='login')
def registerUser(request):
    form = CriarUsuario()

    if request.method == 'POST':
        form = CriarUsuario(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta foi criada com sucesso!')        
            

    context = {'form': form}

    return render(request, 'registro.html', context)

@login_required(login_url='login')
def homepage(request):
    pacientes = Paciente.objects.all() # Retornar toda lista dos pacientes
    consultas = Consulta.objects.all() # Retornar toda lista das consultas

    total_consultas = consultas.count() # Quantidade geral de consultas 
    confirmadas = consultas.filter(status='Confirmada').count() # Quantidade de conultas confirmadas
    concluidas = consultas.filter(status='Concluída').count() # Quantidade de conultas concluídas
        

    ultimas_consultas = Consulta.objects.exclude(status='Concluída').order_by('-data_criacao')[:5]
    ultimas_pacientes = Paciente.objects.order_by('-data_criacao')[:6]

    # Dicionario com variaveis para retorno no template
    context = {'pacientes': pacientes, 'consultas': consultas, 'total_consultas': total_consultas, 'confirmadas': confirmadas, 'concluidas': concluidas, 'ultimas_consultas': ultimas_consultas, 'ultimas_pacientes':ultimas_pacientes}

    return render(request, 'homepage.html', context)

@login_required(login_url='login')
def pacientes(request, nome):
    pacientes = Paciente.objects.get(nome=nome)
    consultas = pacientes.consulta_set.all()

    total_consultas = consultas.count()

    context = {'pacientes': pacientes, 'consultas':consultas, 'total_consultas': total_consultas}
    return render(request, 'pacientes.html', context)

@login_required(login_url='login')
def lista_paciente(request):
    pacientes = Paciente.objects.all()

    context = {'pacientes': pacientes}

    return render(request, 'lista_paciente.html', context)

@login_required(login_url='login')
def marcar_consulta(request, nome):
    paciente = Paciente.objects.get(nome=nome)
    form = ConsultaForm(initial={'paciente':paciente})
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form': form}
    return render(request, 'consultas_form.html', context)

@login_required(login_url='login')
def atualizar_consulta(request, pk):
    consulta = Consulta.objects.get(pk=pk)
    form = ConsultaForm(instance=consulta)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'att_consulta.html', context)

@login_required(login_url='login')
def remover_consulta(request, pk):
    consulta = Consulta.objects.get(pk=pk)
    if request.method == 'POST':
        consulta.delete()
        return redirect('/')
    
    context = {'item': consulta}
    return render(request, 'deletar_consulta.html', context)

@login_required(login_url='login')
def cadastrar_cliente(request):
    form = PacienteForm()
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form': form}
    return render(request, 'pacientes_form.html', context)


@login_required(login_url='login')
def atualizar_cliente(request, nome):
    paciente = Paciente.objects.get(nome=nome)
    form = PacienteAttForm(instance=paciente)
    if request.method == "POST":
        form = PacienteAttForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form': form}
    return render(request, 'atualizar_cliente.html', context)

def custom_404_view(request, exception):
    return render(request, 'errors/404.html', status=404)