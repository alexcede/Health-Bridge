from rest_framework import serializers
from .model import UserSupport
class UserSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSupport
        fields = (
            'id',
            'email',
            'password',
            'name',
            'firstSurname',
            'secondSurname',
            'phoneNumber',
            'active'
        )
