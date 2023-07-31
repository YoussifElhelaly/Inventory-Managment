from django.db import models
from disease.models import Disease
from medicine.models import Medicine


# Create your models here.
class Banlist(models.Model):
    disease = models.OneToOneField(Disease, on_delete=models.CASCADE)
    medicine = models.ManyToManyField(Medicine)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)
