import os

import requests
from django.core.validators import RegexValidator
from django.db import models

from django.utils.translation import gettext_lazy as _


class Mailing(models.Model):
    dt_start = models.DateTimeField(verbose_name='Start time', null=True, blank=True)
    dt_end = models.DateTimeField(verbose_name='End time', null=True, blank=True)
    text = models.TextField(verbose_name='Message')
    mobile_code = models.SmallIntegerField(verbose_name='Mobile operator code')

    class Meta:
        verbose_name = 'Mailing'
        verbose_name_plural = 'Mailings'
        ordering = ['-dt_start']

    def __str__(self):
        return f'{self.mobile_code}, {self.dt_start}'


class Client(models.Model):
    import pytz
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    phone_regex = RegexValidator(regex=r'^7\w{10}$',
                                 message="Phone number must be entered in the format: '999999999'.")
    phone = models.CharField(validators=[phone_regex], max_length=11, blank=True, unique=True)
    mobile_code = models.SmallIntegerField(verbose_name='Mobile operator code')
    tag = models.CharField(verbose_name='Simple tag', max_length=5)
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return f'{self.mobile_code}, {self.tag}'


class Request(models.Model):
    class RequestStatusChoices(models.TextChoices):
        SUCCESS = 'SC', _('SUCCESS')
        FAILED = 'FL', _('FAILED')
        IN_WORK = 'IW', _('IN WORK')
        NEW = 'NEW', _('NEW')

    dt_start = models.DateTimeField(verbose_name='Request start time', null=True, blank=True)
    status = models.TextField(
        choices=RequestStatusChoices.choices,
        default=RequestStatusChoices.NEW
    )
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='request', null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='request')

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'

    def __str__(self):
        return f'{self.client}, {self.status}'
