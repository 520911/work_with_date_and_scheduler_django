from django.contrib import admin
from .models import Mailing, Client, Request


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    pass
