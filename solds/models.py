from django.db import models
from disease.models import Disease
from medicine.models import Medicine
from users.models import User
import random

# Create your models here.


class Sold(models.Model):
    sold_number = models.IntegerField(unique=True)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sold_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    quantities = models.IntegerField(null=True)
    pharmacist = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        number_list = [x for x in range(10)]
        code_items = []

        for i in range(5):
            num = random.choice(number_list)
            code_items.append(num)

        code_string = "".join(str(item) for item in code_items)
        self.sold_number = code_string
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
