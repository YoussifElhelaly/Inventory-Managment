from django.db import models

# Create your models here.

NOTIFICATION_TYPES = (
    ("Item Warning", "Item Warning"),
    ("Expiration Warning", "Expiration Warning"),
)


class Notification(models.Model):
    notification_type = models.CharField(max_length=100, choices=NOTIFICATION_TYPES)
    content = models.CharField(max_length=200)
    bar_code = models.BigIntegerField()
    sent_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    seen = models.BooleanField(default=False)
