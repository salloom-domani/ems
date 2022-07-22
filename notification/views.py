from rest_framework.viewsets import ReadOnlyModelViewSet
from . import models
from . import serializers


class NotificationViewSet(ReadOnlyModelViewSet):
    serializer_class = serializers.NotificationSerializer
    queryset = models.Notification.objects.all()