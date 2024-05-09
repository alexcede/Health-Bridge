from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .model import Report
from .serializer import ReportSerializer

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