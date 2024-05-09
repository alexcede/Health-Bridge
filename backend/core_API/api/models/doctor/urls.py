from django.urls import path
from . import views

# URL's a la api de doctor
urlpatterns = [
    # Endpoints para el doctor
    path('', views.get_all_doctors),
    path('active/', views.get_active_doctors),
    path('no-active/', views.get_no_active_doctors),
    path('<int:id>/', views.get_doctor),
    path('add/', views.add_doctor),
    path('update/<int:id>/', views.update_doctor),
    path('delete/<int:id>/', views.delete_doctor),
    
    # Endpoints para las asignaciones del doctor
    path('assignment/<int:doctor_id>/', views.get_doctor_assignments),  
    path('assignment/active/<int:doctor_id>/', views.get_active_doctor_assignments),  
    path('assignment/no-active/<int:doctor_id>/', views.get_no_active_doctor_assignments), 
    
    # Endpoints para los reportes del doctor
    path('report/get/<int:doctor_id>/', views.get_doctor_reports),
]