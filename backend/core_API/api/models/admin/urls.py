from django.urls import path
from . import views

urlpatterns = [
    # Endpoints para las asignaciones
    path('login/', views.admin_login),
]