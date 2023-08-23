from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import *

def login_view(request):
    error_message = None
    if request.method == 'POST':
        # Procesar el formulario de inicio de sesión
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('task_manager_app:welcome')
        else:
            # Mostrar un mensaje de error en la plantilla
            error_message = "Credenciales incorrectas."
    
    return render(request, 'task_manager_app/login.html', {'error_message': error_message})

def logout_view(request):
    logout(request)
    return redirect('task_manager_app:welcome')

def welcome_view(request):
    return render(request, 'task_manager_app/welcome.html')

def task_list_view(request):
    tasks = Task.objects.filter(user=request.user, state='pendiente').order_by('due_date')
    return render(request, 'task_manager_app/task_list.html', {'tasks': tasks})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_manager_app:login')  # Redirigir al login después de registro exitoso
    else:
        form = UserCreationForm()
    return render(request, 'task_manager_app/register.html', {'form': form})