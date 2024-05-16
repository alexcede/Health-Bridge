from rest_framework import serializers
from .model import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'photo',
            'name',
            'firstSurname',
            'secondSurname',
            'phoneNumber',
            'healthCardCode',
            'birthDate',
            'gender',
            'dni',
            'address',
            'postalCode',
            'active'
        )