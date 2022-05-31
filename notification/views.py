from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers


class NotificationViewSet(ModelViewSet):
    serializer_class = serializers.NotificationSerializer
    queryset = models.Notification.objects.all()