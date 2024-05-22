from django.urls import path
from . import views

urlpatterns = [
    # Endpoints para el usuario
    path('', views.get_all_users),
    path('active/', views.get_active_users),
    path('no-active/', views.get_no_active_users),
    path('<int:id>/', views.get_user),
    path('add/', views.add_user),
    path('update/<int:id>/', views.update_user),
    path('delete/<int:id>/', views.delete_user),
    path('activate/<int:id>/', views.active_user),
    # Endpoints para las asignaciones del usuario
    path('assignment/<int:user_id>/', views.get_user_assignments),
    path('assignment/active/<int:user_id>/', views.get_active_user_assignment),
    path('assignment/no-active/<int:user_id>/', views.get_no_active_user_assignments),
    # Endpoints para los reportes del usuario
    path('report/get/<int:user_id>/', views.get_user_reports),
    
    path('login/', views.user_login),
    path('photo/<str:filename>/', views.get_user_profile_picture)
]