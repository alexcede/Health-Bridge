from django.urls import path
from . import views

urlpatterns = [
    path('addRecipe/', views.create_recipe),
    path('addRecipeInfo/', views.create_recipe_info),
    path('addMedicine/', views.create_medicine) 
]
