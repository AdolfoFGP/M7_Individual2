from django.urls import path
from . import views

app_name = 'task_manager_app'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('welcome/', views.welcome_view, name='welcome'),
    path('tasks/', views.task_list_view, name='task_list'),
    path('register/', views.register_view, name='register'),

    
]
