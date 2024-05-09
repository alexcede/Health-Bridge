from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_report),
    path('update/', views.update_report)
]