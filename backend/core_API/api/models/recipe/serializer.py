from rest_framework import serializers
from .model import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            'id',
            'name',
            'medicine',
            'morning_dose',
            'noon_dose',
            'night_dose',
            'active'
        )