from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from api.models import Admin,Doctor,User,UserSupport,Assignment,Report,Recipe
from api.serializers import AdminSerializer,DoctorSerializer,UserSerializer,UserSupportSerializer,AssignmentSerializer,ReportSerializer,RecipeSerializer

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



