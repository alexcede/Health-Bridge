from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_report),
    path('update/<int:report_id>/', views.update_report),
    path('getAll/', views.get_all_reports)
]