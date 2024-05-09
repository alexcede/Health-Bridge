from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .model import User
from .serializer import UserSerializer
from api.models.assignment.model import Assignment
from api.models.doctor.serializer import DoctorSerializer

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
        
#                             // Asignaciones

#Coje todas las asignaciones del usuario
@csrf_exempt
def get_user_assignments(request, user_id):
    if request.method == 'GET':
        try:
            # Buscar todas las asignaciones del usuario por su ID
            assignments = Assignment.objects.filter(userId=user_id)
            # Serializar los objetos de Doctor y User relacionados
            assignments_data = []
            for assignment in assignments:
                doctor_serializer = DoctorSerializer(assignment.doctorId)
                user_serializer = UserSerializer(assignment.userId)
                # Crear un diccionario con la información de cada asignación
                assignment_data = {
                    'id': assignment.id,
                    'doctor': doctor_serializer.data,
                    'user': user_serializer.data,
                    'dateCreated': assignment.dateCreated
                }
                assignments_data.append(assignment_data)
            return JsonResponse(assignments_data, safe=False)
        except User.DoesNotExist:
            return JsonResponse("Usuario no encontrado.", status=404, safe=False)

# Coje la ultima asignacion del
@csrf_exempt
def get_active_user_assignment(request, user_id):
    if request.method == 'GET':
        try:
            # Buscar todas las asignaciones activas del usuario por su ID
            assignments = Assignment.objects.filter(userId=user_id, active=True)
            # Verificar si se encontraron asignaciones activas para el usuario
            if assignments.exists():
                # Serializar las asignaciones activas
                assignments_data = []
                for assignment in assignments:
                    doctor_serializer = DoctorSerializer(assignment.doctorId)
                    user_serializer = UserSerializer(assignment.userId)
                    assignment_data = {
                        'id': assignment.id,
                        'doctor': doctor_serializer.data,
                        'user': user_serializer.data,
                        'dateCreated': assignment.dateCreated
                    }
                    assignments_data.append(assignment_data)
                return JsonResponse(assignments_data, safe=False)
            else:
                return JsonResponse("No se encontraron asignaciones activas para este usuario.", status=404, safe=False)
        except Assignment.DoesNotExist:
            return JsonResponse("No se encontraron asignaciones para este usuario.", status=404, safe=False)

# Cojer todos las asignaciones no activas del usuario
def get_no_active_user_assignments(request, user_id):
    if request.method == 'GET':
        try:
            # Buscar todas las asignaciones inactivas del usuario por su ID
            assignments = Assignment.objects.filter(userId=user_id, active=False)
            # Verificar si se encontraron asignaciones inactivas para el usuario
            if assignments.exists():
                # Serializar las asignaciones inactivas
                assignments_data = []
                for assignment in assignments:
                    doctor_serializer = DoctorSerializer(assignment.doctorId)
                    user_serializer = UserSerializer(assignment.userId)
                    assignment_data = {
                        'id': assignment.id,
                        'doctor': doctor_serializer.data,
                        'user': user_serializer.data,
                        'dateCreated': assignment.dateCreated
                    }
                    assignments_data.append(assignment_data)
                return JsonResponse(assignments_data, safe=False)
            else:
                return JsonResponse("No se encontraron asignaciones inactivas para este usuario.", status=404, safe=False)
        except Assignment.DoesNotExist:
            return JsonResponse("No se encontraron asignaciones para este usuario.", status=404, safe=False)