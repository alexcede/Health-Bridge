from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .model import UserSupport
from .serializer import UserSupportSerializer

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
