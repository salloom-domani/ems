from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from . import models
from . import serializers


class RequestViewSet(ModelViewSet):
    serializer_class = serializers.RequestSerializer
    queryset = models.Request.objects.all()

    @action(detail=True, methods=['get'])
    def approve(self, request, pk=None):
        request_object = self.get_object()
        request_object.approve(1)
        request_object.save()
        return Response({ 'status': 'Approved successfully!'})
        

class FixRequestViewSet(ModelViewSet):
    serializer_class = serializers.FixRequestSerializer
    queryset = models.FixRequest.objects.all()

class TransferRequestViewSet(ModelViewSet):
    serializer_class = serializers.TransferRequestSerializer
    queryset = models.TransferRequest.objects.all()