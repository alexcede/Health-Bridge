from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .model import Doctor
from .serializer import DoctorSerializer
from api.models.assignment.model import Assignment
from api.models.user.serializer import UserSerializer

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
        
#--------------------------------ASIGNACIONES---------------------------------------------------

# Coje todas las asignaciones del doctor
@csrf_exempt
def get_doctor_assignments(request, doctor_id):
    if request.method == 'GET':
        try:
            # Buscar todas las asignaciones del doctor por su ID
            assignments = Assignment.objects.filter(doctor=doctor_id)
            # Serializar los objetos de Doctor y User relacionados
            assignments_data = []
            for assignment in assignments:
                doctor_serializer = DoctorSerializer(assignment.doctor)
                user_serializer = UserSerializer(assignment.user)
                # Crear un diccionario con la información de cada asignación
                assignment_data = {
                    'id': assignment.id,
                    'doctor': doctor_serializer.data,
                    'user': user_serializer.data,
                    'dateCreated': assignment.dateCreated
                }
                assignments_data.append(assignment_data)
            return JsonResponse(assignments_data, safe=False)
        except Doctor.DoesNotExist:
            return JsonResponse("Doctor no encontrado.", status=404, safe=False)

# Coje todas las asignaciones activas del doctor
@csrf_exempt
def get_active_doctor_assignments(request, doctor_id):
    if request.method == 'GET':
        try:
            # Buscar todas las asignaciones activas del doctor por su ID
            assignments = Assignment.objects.filter(doctor=doctor_id, active=True)
            # Verificar si se encontraron asignaciones activas para el doctor
            if assignments.exists():
                # Serializar las asignaciones activas
                assignments_data = []
                for assignment in assignments:
                    doctor_serializer = DoctorSerializer(assignment.doctor)
                    user_serializer = UserSerializer(assignment.user)
                    assignment_data = {
                        'id': assignment.id,
                        'doctor': doctor_serializer.data,
                        'user': user_serializer.data,
                        'dateCreated': assignment.dateCreated
                    }
                    assignments_data.append(assignment_data)
                return JsonResponse(assignments_data, safe=False)
            else:
                return JsonResponse("No se encontraron asignaciones activas para este doctor.", status=404, safe=False)
        except Assignment.DoesNotExist:
            return JsonResponse("No se encontraron asignaciones para este doctor.", status=404, safe=False)

# Coje todas las asignaciones inactivas del doctor
@csrf_exempt
def get_no_active_doctor_assignments(request, doctor_id):
    if request.method == 'GET':
        try:
            # Buscar todas las asignaciones inactivas del doctor por su ID
            assignments = Assignment.objects.filter(doctor=doctor_id, active=False)
            # Verificar si se encontraron asignaciones inactivas para el doctor
            if assignments.exists():
                # Serializar las asignaciones inactivas
                assignments_data = []
                for assignment in assignments:
                    doctor_serializer = DoctorSerializer(assignment.doctor)
                    user_serializer = UserSerializer(assignment.user)
                    assignment_data = {
                        'id': assignment.id,
                        'doctor': doctor_serializer.data,
                        'user': user_serializer.data,
                        'dateCreated': assignment.dateCreated
                    }
                    assignments_data.append(assignment_data)
                return JsonResponse(assignments_data, safe=False)
            else:
                return JsonResponse("No se encontraron asignaciones inactivas para este doctor.", status=404, safe=False)
        except Assignment.DoesNotExist:
            return JsonResponse("No se encontraron asignaciones para este doctor.", status=404, safe=False)
        
#-----------------------------------------REPORTES----------------------------------------

# Coje todos los reportes del doctor
@csrf_exempt
def get_doctor_reports(request, doctor_id):
    from api.models.report.model import Report
    if request.method == 'GET':
        try:
            # Buscar todos los reportes del doctor por su ID
            reports = Report.objects.filter(doctor=doctor_id)
            # Verificar si se encontraron reportes para el doctor
            if reports.exists():
                # Serializar los reportes
                reports_data = []
                for report in reports:
                    doctor_serializer = DoctorSerializer(report.doctor)
                    user_serializer = UserSerializer(report.user)
                    report_data = {
                        'id': report.id,
                        'doctor': doctor_serializer.data,
                        'user': user_serializer.data,
                        'reportInfo': report.reportInfo,
                        'dateCreated': report.dateCreated
                    }
                    reports_data.append(report_data)
                return JsonResponse(reports_data, safe=False)
            else:
                return JsonResponse("No se encontraron reportes para este doctor.", status=404, safe=False)
        except Report.DoesNotExist:
            return JsonResponse("No se encontraron reportes para este doctor.", status=404, safe=False)