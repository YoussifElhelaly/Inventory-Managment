from django.db import models
from disease.models import Disease
from medicine.models import Medicine
from users.models import User
from django.utils import timezone
from globals.utils import now

# Create your models here.

year_slice = slice(-1, -2)


class Sold(models.Model):
    sold_number = models.BigIntegerField(unique=True)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sold_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    quantities = models.IntegerField(null=True)
    pharmacist = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        year = str(now.year)[-2:]
        print("year:", year)
        month = f"{now.month:02}"
        print("month:", f"{month:02}")
        day = f"{now.day:02}"
        print("day:", day)
        hour = f"{now.hour:02}"
        print("hour:", hour)
        min = f"{now.minute:02}"
        print("min:", min)
        sec = f"{now.second:02}"
        print("sec:", sec)
        sold_code = f"{year}{month}{day}{hour}{min}{sec}"
        self.sold_number = sold_code
        super().save(*args, **kwargs)


class SoldItem(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    pharmacist = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    sold = models.ForeignKey(Sold, on_delete=models.CASCADE, related_name="sold_items")

    def save(self, *args, **kwargs):
        self.total = self.quantity * self.medicine.price
        super(SoldItem, self).save(*args, **kwargs)
