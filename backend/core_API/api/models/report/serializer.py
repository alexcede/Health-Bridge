from rest_framework import serializers
from .model import Report

class ReportSerializer(serializers.ModelSerializer):
    class meta:
        model = Report
        fields = (
            'id',
            'doctorId',
            'userId',
            'reportInfo',
            'dateCreated'
        )