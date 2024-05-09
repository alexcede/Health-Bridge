from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .model import Assignment
from .serializer import AssignmentSerializer
from api.models.doctor.model import Doctor
from api.models.doctor.serializer import DoctorSerializer
from api.models.user.model import User
from api.models.user.serializer import UserSerializer


# Añade una nueva asignacion
@csrf_exempt
def add_assignment(request):
    if request.method == 'POST':
        try:
            # Obtener los datos de la solicitud en formato JSON
            assignment_data = JSONParser().parse(request)
            
            # Obtener el ID del doctor y del usuario de los datos de la solicitud
            doctor_id = assignment_data.get('doctorId')
            user_id = assignment_data.get('userId')

            # Verificar si el doctor y el usuario existen en la base de datos
            doctor = Doctor.objects.get(id=doctor_id)
            user = User.objects.get(id=user_id)

            # Crear la asignación con los datos proporcionados
            assignment_serializer = AssignmentSerializer(data=assignment_data)
            
            if assignment_serializer.is_valid():
                assignment_serializer.save()
                return JsonResponse("Asignación creada correctamente!", safe=False)
            else:
                return JsonResponse("Los datos de la asignación no son válidos.", status=400, safe=False)
        except Doctor.DoesNotExist:
            return JsonResponse("Doctor no encontrado.", status=404, safe=False)
        except User.DoesNotExist:
            return JsonResponse("Usuario no encontrado.", status=404, safe=False)
    else:
        return JsonResponse("Método no permitido. Se requiere un método POST.", status=405, safe=False)

    
# Coje la asignacion por id
@csrf_exempt
def get_assignment(request, id):
    if request.method == 'GET':
        try:
            # Buscar la asignación por su ID
            assignment = Assignment.objects.get(id=id)
            # Serializar los objetos de Doctor y User relacionados
            doctor_serializer = DoctorSerializer(assignment.doctorId)
            user_serializer = UserSerializer(assignment.userId)
            # Crear un diccionario con la información
            assignment_data = {
                'id': assignment.id,
                'doctor': doctor_serializer.data,
                'user': user_serializer.data,
                'dateCreated': assignment.dateCreated
            }
            return JsonResponse(assignment_data, safe=False)
        except Assignment.DoesNotExist:
            return JsonResponse("Asignación no encontrada.", status=404, safe=False)
        
# Cambiar el campo active a True
@csrf_exempt
def activate_assignment(request, id):
    if request.method == 'PUT':
        try:
            assignment = Assignment.objects.get(id=id)
            assignment.active = True
            assignment.save()
            return JsonResponse("Asignación activada correctamente.", status=200, safe=False)
        except Assignment.DoesNotExist:
            return JsonResponse("Asignación no encontrada.", status=404, safe=False)

# Cambiar el campo active a False
@csrf_exempt
def delete_assignment(request, id):
    if request.method == 'DELETE':
        try:
            assignment = Assignment.objects.get(id=id)
            assignment.active = False
            assignment.save()
            return JsonResponse("Asignación eliminada correctamente.", status=200, safe=False)
        except Assignment.DoesNotExist:
            return JsonResponse("Asignación no encontrada.", status=404, safe=False)