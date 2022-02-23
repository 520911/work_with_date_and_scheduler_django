from rest_framework import serializers

from .models import Client, Request, Mailing


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = ('id', 'dt_start', 'dt_end', 'text', 'mobile_code')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'phone', 'mobile_code', 'tag', 'timezone')


class RequestSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    mailing = MailingSerializer()

    class Meta:
        model = Request
        fields = ('dt_start', 'status', 'client', 'mailing')
