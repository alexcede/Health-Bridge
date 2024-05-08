from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from api.models import Admin,Doctor,User,UserSupport,Assignment,Report,Recipe
from api.serializers import AdminSerializer,DoctorSerializer,UserSerializer,UserSupportSerializer,AssignmentSerializer,RecipeSerializer

#-----------------------------DOCTORS-------------------------------
#Coje a todos los doctores de la base de datos
@csrf_exempt
def get_all_doctors(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return JsonResponse(serializer.data, safe=False)

# Coje al doctor por su id
@csrf_exempt
def get_doctor(request, id):
    if request.method == 'GET':
        doctor = Doctor.objects.filter(id=id).first()
        if doctor:
            serializer = DoctorSerializer(doctor)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse("Doctor no encontrado.", status=404)
        
# Coje a los doctores activos
@csrf_exempt
def get_active_doctors(request):
    if request.method == 'GET':
        doctors = Doctor.objects.filter(active=True)
        if doctors:
            serializer = DoctorSerializer(doctors, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse('No hay medicos activos.', safe=False)
        
# Coje a los doctores no activos
@csrf_exempt
def get_no_active_doctors(request):
    if request.method == 'GET':
        doctors = Doctor.objects.filter(active=False)
        if doctors:
            serializer = DoctorSerializer(doctors, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse('No hay medicos desactivados.', safe=False)
        
# Añade un doctor
@csrf_exempt
def add_doctor(request):
    if request.method == 'POST':
        doctor_data = JSONParser().parse(request)
        doctor_serializer = DoctorSerializer(data=doctor_data)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return JsonResponse("Se ha añadido correctamente!", safe=False)
        return JsonResponse("No se ha podido añadir al doctor.", status=400, safe=False)
    else:
        return JsonResponse("Método no permitido. Se requiere un método POST.", status=405, safe=False)

# Actualiza el medico elegido
@csrf_exempt
def update_doctor(request, id):
    if request.method == 'PUT':
        doctor_data = JSONParser().parse(request)
        doctor = Doctor.objects.get(id=id)
        serializer = DoctorSerializer(doctor, data=doctor_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Se ha actualizado el doctor correctamente!", safe=False)
        return JsonResponse("No se ha podido actualizar al doctor.", safe=False)

# Cambia el estado del campo active a false de un doctor
@csrf_exempt
def delete_doctor(request, id):
    if request.method == 'DELETE':
        try:
            doctor = Doctor.objects.get(id=id)
            doctor.active = False
            doctor.save()
            return JsonResponse("Doctor desactivado correctamente.", status=200, safe=False)
        except Doctor.DoesNotExist:
            return JsonResponse("Doctor no encontrado.", status=404, safe=False)

#----------------------------------------END-DOCTORS----------------------------------------------

#----------------------------------------USERS---------------------------------------------------

# Coje a todos los usuarios de la base de datos
@csrf_exempt
def get_all_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

# Coje al usuario por su id
@csrf_exempt
def get_user(request, id):
    if request.method == 'GET':
        user = User.objects.filter(id=id).first()
        if user:
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse("Usuario no encontrado.", status=404)

# Coje a los usuarios activos
@csrf_exempt
def get_active_users(request):
    if request.method == 'GET':
        users = User.objects.filter(active=True)
        if users:
            serializer = UserSerializer(users, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse('No hay usuarios activos.', safe=False)

# Coje a los usuarios no activos
@csrf_exempt
def get_no_active_users(request):
    if request.method == 'GET':
        users = User.objects.filter(active=False)
        if users:
            serializer = UserSerializer(users, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse('No hay usuarios desactivados.', safe=False)

# Añade un usuario
@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Se ha añadido correctamente!", safe=False)
        return JsonResponse("No se ha podido añadir al usuario.", status=400, safe=False)
    else:
        return JsonResponse("Método no permitido. Se requiere un método POST.", status=405, safe=False)

# Actualiza el usuario elegido
@csrf_exempt
def update_user(request, id):
    if request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data=user_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Se ha actualizado el usuario correctamente!", safe=False)
        return JsonResponse("No se ha podido actualizar al usuario.", safe=False)

# Cambia el estado del campo active a false de un usuario
@csrf_exempt
def delete_user(request, id):
    if request.method == 'DELETE':
        try:
            user = User.objects.get(id=id)
            user.active = False
            user.save()
            return JsonResponse("Usuario desactivado correctamente.", status=200, safe=False)
        except User.DoesNotExist:
            return JsonResponse("Usuario no encontrado.", status=404, safe=False)

#-----------------------------END-USERS----------------------------------------

#-----------------------------USER-SUPPORT-------------------------------------

# Coje a todos los usuarios de soporte
@csrf_exempt
def get_all_user_support(request):
    if request.method == 'GET':
        users_support = UserSupport.objects.all()
        serializer = UserSupportSerializer(users_support, many=True)
        return JsonResponse(serializer.data, safe=False)

# Coje al usuario de soporte por su id
@csrf_exempt
def get_user_support(request, id):
    if request.method == 'GET':
        user_support = UserSupport.objects.filter(id=id).first()
        if user_support:
            serializer = UserSupportSerializer(user_support)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse("Usuario de soporte no encontrado.", status=404)
        
# Coje a los usuarios de soporte activos
@csrf_exempt
def get_active_user_support(request):
    if request.method == 'GET':
        users_support = UserSupport.objects.filter(active=True)
        if users_support:
            serializer = UserSupportSerializer(users_support, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse('No hay usuarios de soporte activos.', safe=False)
        
# Coje a los usuarios de soporte no activos
@csrf_exempt
def get_no_active_user_support(request):
    if request.method == 'GET':
        users_support = UserSupport.objects.filter(active=False)
        if users_support:
            serializer = UserSupportSerializer(users_support, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse('No hay usuarios de soporte desactivados.', safe=False)
        
# Añade un usuario de soporte
@csrf_exempt
def add_user_support(request):
    if request.method == 'POST':
        user_support_data = JSONParser().parse(request)
        user_support_serializer = UserSupportSerializer(data=user_support_data)
        if user_support_serializer.is_valid():
            user_support_serializer.save()
            return JsonResponse("Se ha añadido correctamente!", safe=False)
        return JsonResponse("No se ha podido añadir al usuario de soporte.", status=400, safe=False)
    else:
        return JsonResponse("Método no permitido. Se requiere un método POST.", status=405, safe=False)

# Actualiza el usuario de soporte elegido
@csrf_exempt
def update_user_support(request, id):
    if request.method == 'PUT':
        user_support_data = JSONParser().parse(request)
        user_support = UserSupport.objects.get(id=id)
        serializer = UserSupportSerializer(user_support, data=user_support_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Se ha actualizado el usuario de soporte correctamente!", safe=False)
        return JsonResponse("No se ha podido actualizar al usuario de soporte.", safe=False)

# Cambia el estado del campo active a false de un usuario de soporte
@csrf_exempt
def delete_user_support(request, id):
    if request.method == 'DELETE':
        try:
            user_support = UserSupport.objects.get(id=id)
            user_support.active = False
            user_support.save()
            return JsonResponse("Usuario de soporte desactivado correctamente.", status=200, safe=False)
        except UserSupport.DoesNotExist:
            return JsonResponse("Usuario de soporte no encontrado.", status=404, safe=False)

