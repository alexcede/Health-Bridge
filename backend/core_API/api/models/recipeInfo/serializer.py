from rest_framework import serializers
from .model import RecipeInfo

class RecipeInfoSerializer(serializers.ModelSerializer):
    class meta:
        model = RecipeInfo
        fields = (
            'id',
            'doctor',
            'user',
            'report',
            'dateFinish',
            'dateCreated',
            'active'
        )