from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from api.models import Admin,Doctor,User,UserSupport,Assignment,Report,Recipe
from api.serializers import AdminSerializer,DoctorSerializer,UserSerializer,UserSupportSerializer,AssignmentSerializer,RecipeSerializer

# Create your views here.
@csrf_exempt
def doctorApi(request,id=0):
    if request.method == 'GET':
        doctors = Doctor.objects.all()
        doctors_serializer = DoctorSerializer(doctors, many = True)
        return JsonResponse(doctors_serializer.data, safe = False)
    
    elif request.method == 'POST':
        doctor_data = JSONParser().parse(request)
        doctor_serializer = DoctorSerializer(data = doctor_data)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return JsonResponse("Se ha añadido correctamente!", safe=False)
        return JsonResponse("No se ha podido añadir al doctor.", safe=False)
    
    elif request.method == 'PUT':
        doctor_data = JSONParser().parse(request)
        doctor = Doctor.objects.get(DoctorId = doctor_data['id'])
        doctor_serializer = DoctorSerializer(doctor,data = doctor_data)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return JsonResponse("Se ha actualizado el doctor correctamente!",safe = False)
        return JsonResponse("No se ha podido actualizar al doctor.",safe = False)
    
    elif request.method == 'DELETE':
        doctor_id = id
        if doctor_id is None:
            return JsonResponse("ID de doctor no proporcionado en la solicitud", status=400)
        try:
            doctor = Doctor.objects.get(pk=doctor_id)
        except Doctor.DoesNotExist:
            return JsonResponse(f"No se encontró un doctor con ID {doctor_id}", status=404)
        doctor.deleted = True
        doctor.save()
        return JsonResponse("El doctor ha sido marcado como eliminado correctamente", safe=False)
    
@csrf_exempt
def adminApi(request,id=0):
    if request.method == 'GET':
        admins = Doctor.objects.all()
        admins_serializer = AdminSerializer(admins, many = True)
        return JsonResponse(admins_serializer.data, safe = False)
    
    elif request.method == 'POST':
        admin_data = JSONParser().parse(request)
        admin_serializer = AdminSerializer(data = admin_data)
        if admin_serializer.is_valid():
            admin_serializer.save()
            return JsonResponse("Se ha añadido correctamente!", safe=False)
        return JsonResponse("No se ha podido añadir al admin.", safe=False)
    
    elif request.method == 'PUT':
        admin_data = JSONParser().parse(request)
        admin = Admin.objects.get(AdminId = admin_data['id'])
        admin_serializer = AdminSerializer(admin,data = admin_data)
        if admin_serializer.is_valid():
            admin_serializer.save()
            return JsonResponse("Se ha actualizado el admin correctamente!",safe = False)
        return JsonResponse("No se ha podido actualizar al admin.",safe = False)
        
@csrf_exempt
def userApi(request,id=0):
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = AdminSerializer(users, many = True)
        return JsonResponse(users_serializer.data, safe = False)
    
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data = user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Se ha añadido correctamente!", safe=False)
        return JsonResponse("No se ha podido añadir al admin.", safe=False)
    
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(UserId = user_data['id'])
        user_serializer = AdminSerializer(user,data = user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Se ha actualizado el user correctamente!",safe = False)
        return JsonResponse("No se ha podido actualizar al user.",safe = False)
