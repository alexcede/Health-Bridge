from django.urls import path
from api import views

urlpatterns = [
    path('doctor/', views.doctorApi),
    path('doctor/<int:pk>/', views.doctorApi),
]