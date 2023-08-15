from celery import shared_task
from medicine.models import Medicine
from notification.models import Notification, NOTIFICATION_TYPES
from datetime import date
from globals.utils import now


@shared_task(bind=False)
def check_medicines_stock():
    medicines = Medicine.objects.all().iterator()
    for medicine in medicines:
        if medicine.stock <= medicine.stock_warn_limit:
            Notification.objects.create(
                notification_type=NOTIFICATION_TYPES[0][0],
                content="المنتج علي وشك النفاذ من المخزون",
                bar_code=int(medicine.bar_code),
            )


@shared_task(bind=False)
def check_medicines_expiration():
    medicines = Medicine.objects.all().iterator()
    for medicine in medicines:
        days_left = date(now.year, now.month, now.day) - date(
            medicine.exp_date.year, medicine.exp_date.month, medicine.exp_date.day
        )
        if days_left.days < 3:
            Notification.objects.create(
                notification_type=NOTIFICATION_TYPES[1][1],
                content="المنتج علي وشك انتهاء صلاحيته",
                bar_code=int(medicine.bar_code),
            )
