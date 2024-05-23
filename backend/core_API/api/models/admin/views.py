from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .model import Admin
from .serializer import AdminSerializer
import json
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password

from api.fields_validator import validate_unique_fields

@csrf_exempt
def admin_login(request):
    if request.method == 'POST':
        # Verificar si el cuerpo de la solicitud está vacío
        if not request.body:
            return JsonResponse({"error": "Empty request body"}, status=400)

        # Leer el cuerpo de la solicitud como JSON
        body_unicode = request.body.decode('utf-8')
        try:
            admin_data = json.loads(body_unicode)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON in request body"}, status=400)

        email = admin_data.get('email', '')
        password = admin_data.get('password', '')

        # Buscar el usuario por su correo electrónico
        try:
            admin = Admin.objects.get(email=email, active=True)
        except Admin.DoesNotExist:
            return JsonResponse({"error": "Incorrect email or password"}, safe=False)

        # Verificar la contraseña
        if not check_password(password, admin.password):
            return JsonResponse({"error": "Incorrect email or password"}, safe=False)

        # Autenticación exitosa
        admin_data = {
                "id": admin.id,
                "email": admin.email,
                "active": admin.active,
            }
        return JsonResponse({"success": "Login successful", 
                             "token": createToken(admin),
                             "role": "doctor",
                             "user": admin_data
                             },
                             status=200, safe=False)

    # Método no permitido
    return JsonResponse({"error": "Method not allowed. POST method required."}, status=405, safe=False)

def createToken(Admin):
    import jwt
    payload = {
        'admin_id':Admin.id,
        'role': 'admin'
    }
    token = jwt.encode(payload, 'secret_key', algorithm='HS256') 
    return token