from celery import shared_task
from banlist.models import CountSaleDanger


@shared_task
def add_count_sale_danger():
    CountSaleDanger.objects.create()
