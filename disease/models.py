from django.db import models

# Create your models here.


class Disease(models.Model):
    name = models.CharField(max_length=150)
    added_at = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name
