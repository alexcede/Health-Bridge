from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .model import UserSupport
from .serializer import UserSupportSerializer

from django.core.exceptions import ValidationError
import bcrypt
from rest_framework.decorators import api_view

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
    from api.fields_validator import validate_unique_fields
    if request.method == 'POST':
        user_support_data = request.POST.copy()
        
        # Hashear la contraseña
        raw_password = user_support_data.get('password', '')  
        hashed_password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())

        # Reemplazar la contraseña en texto plano por la contraseña hasheada en los datos del user
        user_support_data['password'] = hashed_password.decode('utf-8')
        
        try:
            # Ejecutar la validación de campos únicos
            unique_errors = validate_unique_fields(user_support_data)
            if unique_errors:
                return JsonResponse({"error": unique_errors}, status=400)
        except ValidationError as e:
            # Capturar errores de validación y devolverlos en formato JSON
            return JsonResponse({"error": e.message_dict}, status=400)

        user_support_serializer = UserSupportSerializer(data=user_support_data)
        
        if user_support_serializer.is_valid():
            user_support_serializer.save()
            return JsonResponse("Se ha añadido correctamente!", safe=False)
        return JsonResponse("No se ha podido añadir al usuario de soporte.", status=400, safe=False)
    else:
        return JsonResponse("Método no permitido. Se requiere un método POST.", status=405, safe=False)

# Actualiza el usuario de soporte elegido
@csrf_exempt
@api_view(['PUT'])
def update_user_support(request, id):
    from api.fields_validator import validate_unique_fields
    if request.method == 'PUT':
        user_support_data = request.data.copy()
        try:
            # Validar campos unicos
            unique_errors = validate_unique_fields(user_support_data)
            if unique_errors:
                return JsonResponse({"error": unique_errors}, status=400, safe=False)
        except ValidationError as e:
            return JsonResponse({"error": e.message_dict}, status=400, safe=False)
        
        try:
            user_support = UserSupport.objects.get(id=id)
            serializer = UserSupportSerializer(user_support, data=user_support_data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse("Se ha actualizado el usuario correctamente!", status=200, safe=False)
        except UserSupport.DoesNotExist:
            return JsonResponse("No se ha encontrado al usuario especificado.", status=400, safe=False)
    else:
        return JsonResponse("Metodo no permitido, Se requiere un metodo PUT", status=405, safe = False)

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
