from rest_framework import serializers
from .model import RecipeInfo

class RecipeInfoSerializer(serializers.ModelSerializer):
    class meta:
        model = RecipeInfo
        fields = (
            'id',
            'doctorId',
            'userId',
            'reportId',
            'dateFinish',
            'dateCreated',
            'active'
        )