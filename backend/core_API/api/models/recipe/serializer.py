from rest_framework import serializers
from .model import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'id',
            'report',
            'dateFinish',
            'dateCreated',
            'active',
        )