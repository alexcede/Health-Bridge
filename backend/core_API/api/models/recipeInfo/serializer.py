from rest_framework import serializers
from .model import RecipeInfo

class RecipeInfoSerializer(serializers.ModelSerializer):
    class meta:
        model = RecipeInfo
        fields = (
            'id',
            'recipe',
            'medicine',
            'morning_dose',
            'noon_dose',
            'night_dose',
            'active'
        )