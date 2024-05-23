from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .model import Recipe
from .serializer import RecipeSerializer

from api.models.recipeInfo.model import RecipeInfo
from api.models.recipeInfo.serializer import RecipeInfoSerializer

from api.models.medicine.model import Medicine
from api.models.medicine.serializer import MedicineSerializer

from api.models.report.model import Report
from api.models.report.serializer import ReportSerializer

# API para crear un nuevo informe (Report)
@csrf_exempt
def create_report(request):
    if request.method == 'POST':
        report_data = JSONParser().parse(request)
        report_serializer = ReportSerializer(data=report_data)
        if report_serializer.is_valid():
            report_serializer.save()
            return JsonResponse(report_serializer.data, status=200, safe=False)
        return JsonResponse(report_serializer.errors, status=400, safe=False)

# API para crear una nueva receta (Recipe)
@csrf_exempt
def create_recipe(request):
    if request.method == 'POST':
        recipe_data = JSONParser().parse(request)
        recipe_serializer = RecipeSerializer(data=recipe_data)
        if recipe_serializer.is_valid():
            recipe_serializer.save()
            return JsonResponse(recipe_serializer.data, status=200, safe=False)
        return JsonResponse(recipe_serializer.errors, status=400, safe=False)

# API para crear una nueva información de receta (RecipeInfo)
@csrf_exempt
def create_recipe_info(request):
    if request.method == 'POST':
        recipe_info_data = JSONParser().parse(request)
        recipe_info_serializer = RecipeInfoSerializer(data=recipe_info_data)
        if recipe_info_serializer.is_valid():
            recipe_info_serializer.save()
            return JsonResponse(recipe_info_serializer.data, status = 200, safe=False)
        return JsonResponse(recipe_info_serializer.errors, status=400, safe=False)

# API para crear un nuevo medicamento (Medicine)
@csrf_exempt
def create_medicine(request):
    if request.method == 'POST':
        medicine_data = JSONParser().parse(request)
        medicine_serializer = MedicineSerializer(data=medicine_data)
        if medicine_serializer.is_valid():
            medicine_serializer.save()
            return JsonResponse(medicine_serializer.data, status=200, safe=False)
        return JsonResponse(medicine_serializer.errors, status=400, safe=False)