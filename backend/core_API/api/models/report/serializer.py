from rest_framework import serializers
from .model import Report

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = (
            'id',
            'doctorId',
            'userId',
            'reportName',
            'disease',
            'reportInfo',
            'dateCreated'
        )