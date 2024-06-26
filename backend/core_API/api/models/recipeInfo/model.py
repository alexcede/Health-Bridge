from django.db import models
from api.models.recipe.model import Recipe
from api.models.medicine.model import Medicine
class RecipeInfo(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT)
    medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT)
    morning_dose = models.DecimalField(max_digits=2, decimal_places=1, choices=[(1, '1'), (0.5, '0.5'), (0, '0')])
    noon_dose = models.DecimalField(max_digits=2, decimal_places=1, choices=[(1, '1'), (0.5, '0.5'), (0, '0')])
    night_dose = models.DecimalField(max_digits=2, decimal_places=1, choices=[(1, '1'), (0.5, '0.5'), (0, '0')])
    active = models.BooleanField(default=True)
