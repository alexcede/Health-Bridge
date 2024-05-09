from django.urls import path
from . import views

urlpatterns = [
    # Endpoints para las asignaciones
    path('add/', views.add_assignment),  
    path('<int:id>/', views.get_assignment),  
    path('activate/<int:id>/', views.activate_assignment), 
    path('delete/<int:id>/', views.delete_assignment),  
]