from rest_framework import serializers
from .model import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class meta:
        model = Recipe
        fields = (
            'id',
            'doctorId',
            'userId',
            'reportId',
            'medicine',
            'dateCreated'
        )