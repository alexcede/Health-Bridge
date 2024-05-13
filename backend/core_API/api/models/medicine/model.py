from django.db import models

class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    dosis = models.CharField(max_length=255, default=None)
    morningDosis = models.DecimalField(max_digits=2, decimal_places=1, choices=[(1, '1'), (0.5, '0.5'), (0, '0')])
    noonDosis = models.DecimalField(max_digits=2, decimal_places=1, choices=[(1, '1'), (0.5, '0.5'), (0, '0')])
    nightDosis = models.DecimalField(max_digits=2, decimal_places=1, choices=[(1, '1'), (0.5, '0.5'), (0, '0')])