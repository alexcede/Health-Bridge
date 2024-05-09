from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_user_support),
    path('active/', views.get_active_user_support),
    path('no-active/', views.get_no_active_user_support),
    path('<int:id>/', views.get_user_support),
    path('add/', views.add_user_support),
    path('update/<int:id>/', views.update_user_support),
    path('delete/<int:id>/', views.delete_user_support),
]