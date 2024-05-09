from rest_framework import serializers
from .model import Assignment

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = (
            'id',
            'doctorId',
            'userId',
            'dateCreated',
            'active'
        )