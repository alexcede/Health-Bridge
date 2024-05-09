from rest_framework import serializers
from .model import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = (
            'id',
            'email',
            'password',
            'dni',
            'photo',
            'name',
            'firstSurname',
            'secondSurname',
            'phoneNumber',
            'active'
        )