from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ClientViewSet, MailingViewSet

client_router = DefaultRouter()
client_router.register('clients', ClientViewSet, basename='clients')

mailing_router = DefaultRouter()
mailing_router.register('mailing', MailingViewSet, basename='mailing')

urlpatterns = [
    path('', include(client_router.urls)),
    path('', include(mailing_router.urls)),
]
