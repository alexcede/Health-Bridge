from django.urls import path
from api import views

urlpatterns = [
    # URL's a la api de doctor
    path('doctors/', views.get_all_doctors),
    path('doctors/active', views.get_active_doctors),
    path('doctors/no-active', views.get_no_active_doctors),
    path('doctor/<int:id>', views.get_doctor),
    path('doctor/add', views.add_doctor),
    path('doctor/update/<int:id>', views.update_doctor),
    path('doctor/delete/<int:id>', views.delete_doctor),
    
    # URL's a la api de user
    path('users/', views.get_all_users),
    path('users/active', views.get_active_users),
    path('users/no-active', views.get_no_active_users),
    path('user/<int:id>', views.get_user),
    path('user/add', views.add_user),
    path('user/update/<int:id>', views.update_user),
    path('user/delete/<int:id>', views.delete_user),
    
    # URL's a la api de usuario de soporte
    path('user_supports/', views.get_all_user_support),
    path('user_supports/active', views.get_active_user_support),
    path('user_supports/no-active', views.get_no_active_user_support),
    path('user_support/<int:id>', views.get_user_support),
    path('user_support/add', views.add_user_support),
    path('user_support/update/<int:id>', views.update_user_support),
    path('user_support/delete/<int:id>', views.delete_user_support),
]