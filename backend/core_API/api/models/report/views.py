from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .model import Report
from .serializer import ReportSerializer

# Obtiene todos los reportes
@csrf_exempt
def get_all_reports(request):
    if request.method == 'GET':
        reports = Report.objects.all()
        report_serializer = ReportSerializer(reports, many=True)
        return JsonResponse(report_serializer.data, safe=False)
    else:
        return JsonResponse("Método no permitido", status=405)

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
    try:
        report = Report.objects.get(id=report_id)
    except Report.DoesNotExist:
        return JsonResponse("Reporte no encontrado.", status=404, safe=False)

    if request.method == 'PUT':
        report_data = JSONParser().parse(request)
        # Actualizar solo el campo reportInfo si está presente en los datos proporcionados
        if 'reportInfo' in report_data:
            report.reportInfo = report_data['reportInfo']
            # Actualizar otros campos si están presentes en los datos proporcionados
            if 'doctorId' in report_data:
                report.doctorId = report_data['doctorId']
            if 'userId' in report_data:
                report.userId = report_data['userId']
            if 'reportName' in report_data:
                report.reportName = report_data['reportName']
            if 'disease' in report_data:
                report.disease = report_data['disease']
            report.save()
            return JsonResponse("Reporte actualizado correctamente!", safe=False)
        else:
            return JsonResponse("El campo 'reportInfo' es requerido para actualizar el reporte.", status=400, safe=False)
        
