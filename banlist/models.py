from django.db import models
from disease.models import Disease
from medicine.models import Medicine, Category


# Create your models here.
class Banlist(models.Model):
    disease = models.OneToOneField(Disease, on_delete=models.CASCADE)
    medicine = models.ManyToManyField(Medicine)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)


class DangerList(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    medicine = models.ManyToManyField(Medicine)
    created_at = models.DateField(auto_created=True, blank=True, null=True)
