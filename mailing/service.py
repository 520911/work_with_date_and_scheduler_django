from datetime import datetime

import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django.db.models.signals import post_save
from django.dispatch import receiver

from mailing.tasks import post_request
from .models import Mailing


@receiver(signal=post_save, sender=Mailing)
def mailing_request(sender, instance=None, created=False, **kwargs):
    if created:
        scheduler = BackgroundScheduler()
        scheduler.start()
        if instance.dt_start <= pytz.utc.localize(datetime.now()) and \
                instance.dt_end > pytz.utc.localize(datetime.now()):
            scheduler.add_job(
                post_request,
                trigger=CronTrigger(start_date=datetime.now()),
                args=[instance.id],
                id=f"_job",
                max_instances=1,
                replace_existing=True,
            )
        else:
            scheduler.add_job(
                post_request,
                trigger=CronTrigger(start_date=instance.dt_start),
                args=[instance.id],
                id=f"__job",
                max_instances=1,
                replace_existing=True,
            )
