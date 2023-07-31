from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=75)
    added_at = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    solds_count = models.BigIntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    prod_date = models.DateField(null=True, blank=True)
    exp_date = models.DateField(null=True, blank=True)
    medicine_img = models.ImageField(upload_to="medicine_images/")
    stock = models.IntegerField()
    stock_warn_limit = models.IntegerField()
    bar_code = models.BigIntegerField()
    added_at = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name
