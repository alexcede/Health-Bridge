from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import HttpResponse, Http404
from .model import User
from .serializer import UserSerializer
from api.models.medicine.model import Medicine
from api.models.recipe.model import Recipe
from api.models.recipeInfo.model import RecipeInfo
from api.models.report.model import Report
from django.core.files.storage import default_storage
from django.conf import settings
import os
import bcrypt
import json
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view

from django.core.exceptions import ValidationError

@csrf_exempt
def get_user_profile_picture(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, 'users', filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    else:
        raise Http404

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        # Verificar si el cuerpo de la solicitud está vacío
        if not request.body:
            return JsonResponse({"error": "Empty request body"}, status=400)

        # Leer el cuerpo de la solicitud como JSON
        body_unicode = request.body.decode('utf-8')
        try:
            user_data = json.loads(body_unicode)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON in request body"}, status=400)

        email = user_data.get('email', '')
        password = user_data.get('password', '')

        # Buscar el usuario por su correo electrónico
        try:
            user = User.objects.get(email=email, active=True)
        except User.DoesNotExist:
            return JsonResponse({"error": "Incorrect email or password"}, safe=False)

        # Verificar la contraseña
        if not check_password(password, user.password):
            return JsonResponse({"error": "Incorrect email or password"}, safe=False)

        # Autenticación exitosa
        user_data = {
                "id": user.id,
                "email": user.email,
                "photo": user.photo,
                "name": user.name,
                "firstSurname": user.firstSurname,
                "secondSurname": user.secondSurname,
                "phoneNumber": user.phoneNumber,
                "healthCardCode": user.healthCardCode,
                "birthDate": user.birthDate.isoformat(),
                "gender": user.gender,
                "dni": user.dni,
                "address": user.address,
                "postalCode": user.postalCode,
                "active": user.active,
            }
        return JsonResponse({"success": "Login successful", 
                             "token": createToken(user),
                             "role": "user",
                             "user": user_data
                             },
                             status=200, safe=False)

    # Método no permitido
    return JsonResponse({"error": "Method not allowed. POST method required."}, status=405, safe=False)

def createToken(User):
    import jwt
    payload = {
        'user_id':User.id,
        'role': 'user'
    }
    token = jwt.encode(payload, 'secret_key', algorithm='HS256') 
    return token

@csrf_exempt
def get_user_recipes(request, id):
    try:
        # Filtrar los informes del usuario específico
        user_reports = Report.objects.filter(user_id=id)
        
        user_recipes = []
        
        # Para cada informe del usuario, obtener las recetas relacionadas
        for report in user_reports:
            report_recipes = Recipe.objects.filter(report_id=report.id)
            
            for recipe in report_recipes:
                # Obtener los detalles de la receta (Medicamentos y dosis)
                recipe_infos = RecipeInfo.objects.filter(recipe_id=recipe.id)
                
                medicines = []
                for recipe_info in recipe_infos:
                    medicine = Medicine.objects.get(id=recipe_info.medicine_id)
                    medicines.append({
                        'medicine_id': medicine.id,
                        'medicine_name': medicine.name,
                        'morning_dose': recipe_info.morning_dose,
                        'noon_dose': recipe_info.noon_dose,
                        'night_dose': recipe_info.night_dose,
                        'total_dose': recipe_info.morning_dose + recipe_info.noon_dose + recipe_info.night_dose
                    })
                
                user_recipes.append({
                    'report_id': report.id,
                    'report_name': report.reportName,
                    'disease': report.disease,
                    'report_info': report.reportInfo,
                    'date_created': report.dateCreated,
                    'recipe_id': recipe.id,
                    'date_finish': recipe.dateFinish,
                    'medicines': medicines
                })
        
        return JsonResponse({'user_recipes': user_recipes}, safe=False)
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

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
    from api.fields_validator import validate_unique_fields
    if request.method == 'POST':
        # Obtener la ruta base de la carpeta de medios
        media_root = settings.MEDIA_ROOT
        # Acceder a los datos de formulario y archivos adjuntos en la solicitud POST
        user_data = request.POST.copy()
        file = request.FILES.get('photo', None)
        
        # Hashear la contraseña
        raw_password = user_data.get('password', '')  
        hashed_password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())

        # Reemplazar la contraseña en texto plano por la contraseña hasheada en los datos del user
        user_data['password'] = hashed_password.decode('utf-8')
        try:
            # Ejecutar la validación de campos únicos
            unique_errors = validate_unique_fields(user_data)
            if unique_errors:
                return JsonResponse({"error": unique_errors}, status=400)
        except ValidationError as e:
            # Capturar errores de validación y devolverlos en formato JSON
            return JsonResponse({"error": e.message_dict}, status=400)

        # Guardar la foto y obtener su ruta
        if file:
            file_extension = file.name.split('.')[-1]  # Obtener la extensión del archivo
            new_file_name = f"{user_data.get('dni')}.{file_extension}"  # Construir el nuevo nombre del archivo
            # Guardar el archivo en el directorio de medios
            file_path = os.path.join(settings.MEDIA_ROOT, 'users', new_file_name)
            with default_storage.open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            # Actualizar el campo 'photo' del user con la ruta de la foto guardada
            file_path_photo = new_file_name
            user_data['photo'] = file_path_photo
        else:
            file_path_photo = 'default.jpg'
            user_data['photo'] = file_path_photo
        
        # Serializar y guardar los datos del user
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Se ha añadido correctamente!", safe=False)
        return JsonResponse("No se ha podido añadir al user.", status=400, safe=False)
    else:
        return JsonResponse("Método no permitido. Se requiere un método POST.", status=405, safe=False)

# Actualiza el usuario elegido
@csrf_exempt
@api_view(['PUT'])
def update_user(request, id):
    from api.fields_validator import validate_unique_fields
    if request.method == 'PUT':
        # Verificar si se están actualizando campos únicos
        user_data = request.data.copy()
        try:
            # Ejecutar la validación de campos únicos
            unique_errors = validate_unique_fields(user_data)
            if unique_errors:
                return JsonResponse({"error": unique_errors}, status=400, safe=False)
        except ValidationError as e:
            # Capturar errores de validación y devolverlos en formato JSON
            return JsonResponse({"error": e.message_dict}, status=400, safe=False)

        try:
            # Obtener el usuario existente
            user = User.objects.get(id=id)

            # Verificar si se está actualizando la foto
            file = request.FILES.get('photo')
            if file:
                file_extension = file.name.split('.')[-1]
                if user_data.get('dni') is None:
                    new_file_name = f"{user.dni}.{file_extension}"
                else:
                    new_file_name = f"{user_data.get('dni')}.{file_extension}"

                # Eliminar el archivo anterior asociado al antiguo DNI del usuario
                old_file_name = f"{user.dni}.{file_extension}"
                old_file_path = os.path.join(settings.MEDIA_ROOT, 'users', old_file_name)
                if os.path.exists(old_file_path):
                    os.remove(old_file_path)

                # Guardar el nuevo archivo
                file_path = os.path.join(settings.MEDIA_ROOT, 'users', new_file_name)
                with default_storage.open(file_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                file_path_photo = '/backend/core_API/media/users/' + new_file_name
                user_data['photo'] = file_path_photo

            # Serializar y guardar los datos actualizados del usuario
            serializer = UserSerializer(user, data=user_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse("Se ha actualizado el usuario correctamente!", status=200, safe=False)
            return JsonResponse(serializer.errors, status=400, safe=False)
        except User.DoesNotExist:
            return JsonResponse("No se ha encontrado el usuario especificado.", status=400, safe=False)
    else:
        return JsonResponse("Método no permitido. Se requiere un método PUT.", status=405, safe=False)

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
        
@csrf_exempt
def active_user(request, id):
    if request.method == 'GET':
        try:
            user = User.objects.get(id=id)
            user.active = True
            user.save()
            return JsonResponse("Usuario desactivado correctamente.", status=200, safe=False)
        except User.DoesNotExist:
            return JsonResponse("Usuario no encontrado.", status=404, safe=False)
        
#                             // Asignaciones

#Coje todas las asignaciones del usuario
@csrf_exempt
def get_user_assignments(request, user_id):
    from api.models.assignment.model import Assignment
    from api.models.doctor.serializer import DoctorSerializer
    if request.method == 'GET':
        try:
            # Buscar todas las asignaciones del usuario por su ID
            assignments = Assignment.objects.filter(user=user_id)
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
        except User.DoesNotExist:
            return JsonResponse("Usuario no encontrado.", status=404, safe=False)

# Coje la ultima asignacion del
@csrf_exempt
def get_active_user_assignment(request, user_id):
    from api.models.assignment.model import Assignment
    from api.models.doctor.serializer import DoctorSerializer
    if request.method == 'GET':
        try:
            # Buscar todas las asignaciones activas del usuario por su ID
            assignments = Assignment.objects.filter(user=user_id, active=True)
            # Verificar si se encontraron asignaciones activas para el usuario
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
                return JsonResponse("No se encontraron asignaciones activas para este usuario.", status=404, safe=False)
        except Assignment.DoesNotExist:
            return JsonResponse("No se encontraron asignaciones para este usuario.", status=404, safe=False)

# Cojer todos las asignaciones no activas del usuario
def get_no_active_user_assignments(request, user_id):
    from api.models.assignment.model import Assignment
    from api.models.doctor.serializer import DoctorSerializer
    if request.method == 'GET':
        try:
            # Buscar todas las asignaciones inactivas del usuario por su ID
            assignments = Assignment.objects.filter(user=user_id, active=False)
            # Verificar si se encontraron asignaciones inactivas para el usuario
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
                return JsonResponse("No se encontraron asignaciones inactivas para este usuario.", status=404, safe=False)
        except Assignment.DoesNotExist:
            return JsonResponse("No se encontraron asignaciones para este usuario.", status=404, safe=False)
        
#                                 REPORTES

# Coje todos los reportes del usuario
@csrf_exempt
def get_user_reports(request, user_id):
    from api.models.report.model import Report
    from api.models.doctor.serializer import DoctorSerializer
    if request.method == 'GET':
        try:
            # Buscar todos los reportes del usuario por su ID
            reports = Report.objects.filter(user=user_id)
            # Verificar si se encontraron reportes para el usuario
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
                return JsonResponse("No se encontraron reportes para este usuario.", status=404, safe=False)
        except Report.DoesNotExist:
            return JsonResponse("No se encontraron reportes para este usuario.", status=404, safe=False)