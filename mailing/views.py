import os
from datetime import datetime

import pytz
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Client, Request, Mailing
from .serializers import MailingSerializer, ClientSerializer, RequestSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MailingViewSet(ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer


class RequestViewSet(ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
