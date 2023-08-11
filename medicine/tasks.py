from celery import shared_task
from medicine.models import Medicine
from notification.models import Notification, NOTIFICATION_TYPES
from dateutil import relativedelta
from globals.utils import now
from django_celery_beat.models import PeriodicTask, IntervalSchedule


schedule, created = IntervalSchedule.objects.get_or_create(
    every=10, period=IntervalSchedule.MINUTES
)


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


PeriodicTask.objects.create(
    interval=schedule,
    name="Check Medicines Stock",
    task="medicine.tasks.check_medicines_stock",
)


@shared_task(bind=False)
def check_medicines_expiration():
    medicines = Medicine.objects.all().iterator()
    for medicine in medicines:
        days_left = relativedelta.relativedelta(now, medicine.exp_date)
        if days_left < 3:
            Notification.objects.create(
                notification_type=NOTIFICATION_TYPES[1][1],
                content="المنتج علي وشك انتهاء صلاحيته",
                bar_code=int(medicine.bar_code),
            )


PeriodicTask.objects.create(
    interval=schedule,
    name="Check Medicines Expiration",
    task="medicine.tasks.check_medicines_expiration",
)
