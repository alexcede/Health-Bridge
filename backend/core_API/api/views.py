from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from api.models import Admin,Doctor,User,UserSupport,Assignment,Report,Recipe
from api.serializers import AdminSerializer,DoctorSerializer,UserSerializer,UserSupportSerializer,AssignmentSerializer,ReportSerializer,RecipeSerializer

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
        
#-------------------------------END-USER-SUPPORT----------------------------------------------------------

#-------------------------------ASSIGNMENT------------------------------------------

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

# Coje todas las asignaciones del doctor
@csrf_exempt
def get_doctor_assignments(request, doctor_id):
    if request.method == 'GET':
        try:
            # Buscar todas las asignaciones del doctor por su ID
            assignments = Assignment.objects.filter(doctorId=doctor_id)
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
        except Doctor.DoesNotExist:
            return JsonResponse("Doctor no encontrado.", status=404, safe=False)

# Coje todas las asignaciones activas del doctor
@csrf_exempt
def get_active_doctor_assignments(request, doctor_id):
    if request.method == 'GET':
        try:
            # Buscar todas las asignaciones activas del doctor por su ID
            assignments = Assignment.objects.filter(doctorId=doctor_id, active=True)
            # Verificar si se encontraron asignaciones activas para el doctor
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
                return JsonResponse("No se encontraron asignaciones activas para este doctor.", status=404, safe=False)
        except Assignment.DoesNotExist:
            return JsonResponse("No se encontraron asignaciones para este doctor.", status=404, safe=False)

# Coje todas las asignaciones inactivas del doctor
@csrf_exempt
def get_no_active_doctor_assignments(request, doctor_id):
    if request.method == 'GET':
        try:
            # Buscar todas las asignaciones inactivas del doctor por su ID
            assignments = Assignment.objects.filter(doctorId=doctor_id, active=False)
            # Verificar si se encontraron asignaciones inactivas para el doctor
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
                return JsonResponse("No se encontraron asignaciones inactivas para este doctor.", status=404, safe=False)
        except Assignment.DoesNotExist:
            return JsonResponse("No se encontraron asignaciones para este doctor.", status=404, safe=False)

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
        
#------------------------------------------END ASSIGNMENTS---------------------------------

#-------------------------------------REPORTS----------------------------------------------

# Añade un nuevo reporte
@csrf_exempt
def add_report(request):
    if request.method == 'POST':
        report_data = JSONParser().parse(request)
        report_serializer = ReportSerializer(data=report_data)
        if report_serializer.is_valid():
            report_serializer.save()
            return JsonResponse("Reporte añadido correctamente!", safe=False)
        return JsonResponse("No se pudo añadir el reporte.", status=400, safe=False)
    else:
        return JsonResponse("Método no permitido. Se requiere un método POST.", status=405, safe=False)

# Actualiza un reporte existente
@csrf_exempt
def update_report(request, report_id):
    if request.method == 'PUT':
        try:
            report = Report.objects.get(id=report_id)
            report_data = JSONParser().parse(request)
            report_serializer = ReportSerializer(report, data=report_data)
            if report_serializer.is_valid():
                report_serializer.save()
                return JsonResponse("Reporte actualizado correctamente!", safe=False)
            return JsonResponse("No se pudo actualizar el reporte.", status=400, safe=False)
        except Report.DoesNotExist:
            return JsonResponse("Reporte no encontrado.", status=404, safe=False)

# Coje todos los reportes del usuario
@csrf_exempt
def get_user_reports(request, user_id):
    if request.method == 'GET':
        try:
            # Buscar todos los reportes del usuario por su ID
            reports = Report.objects.filter(userId=user_id)
            # Verificar si se encontraron reportes para el usuario
            if reports.exists():
                # Serializar los reportes
                reports_data = []
                for report in reports:
                    doctor_serializer = DoctorSerializer(report.doctorId)
                    user_serializer = UserSerializer(report.userId)
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
                return JsonResponse("No se encontraron reportes para este usuario.", status=404, safe=False)
        except Report.DoesNotExist:
            return JsonResponse("No se encontraron reportes para este usuario.", status=404, safe=False)

# Coje todos los reportes del doctor
@csrf_exempt
def get_doctor_reports(request, doctor_id):
    if request.method == 'GET':
        try:
            # Buscar todos los reportes del doctor por su ID
            reports = Report.objects.filter(doctorId=doctor_id)
            # Verificar si se encontraron reportes para el doctor
            if reports.exists():
                # Serializar los reportes
                reports_data = []
                for report in reports:
                    doctor_serializer = DoctorSerializer(report.doctorId)
                    user_serializer = UserSerializer(report.userId)
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



