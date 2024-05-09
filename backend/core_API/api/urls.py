from django.urls import path, include

urlpatterns = [
    # URL a la api de doctor
    path('doctor/', include('api.models.doctor.urls')),
    # URL a la api de user
    path('user/', include('api.models.user.urls')),
    # URL a la api de usuario de soporte
    path('user_support/', include('api.models.user_support.urls')),
    # URL para las asignaciones
    path('assignment/', include('api.models.assignment.urls')), 
    # URL para los reportes
    path('report/', include('api.models.report.urls')),
]