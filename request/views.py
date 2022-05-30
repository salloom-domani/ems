from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers


class RequestViewSet(ModelViewSet):
    serializer_class = serializers.RequestSerializer
    queryset = models.Request.objects.all()

class FixRequestViewSet(ModelViewSet):
    serializer_class = serializers.FixRequestSerializer
    queryset = models.FixRequest.objects.all()

class TransferRequestViewSet(ModelViewSet):
    serializer_class = serializers.TransferRequestSerializer
    queryset = models.TransferRequest.objects.all()