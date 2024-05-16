from rest_framework import serializers
from .model import Admin
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = (
            'id',
            'email',
            'password',
            'active'
        )
