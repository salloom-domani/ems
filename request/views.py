from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from . import models
from . import serializers


class RequestViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = models.Request.objects.all()

    @action(detail=True, methods=['GET'])
    def approve(self, request, pk=None):
        request_object = self.get_object()
        request_object.approve(1)
        request_object.save()
        return Response({"status": "Approved successfully!"})

    def get_serializer_class(self):
        if self.request.method == "PUT":
            return serializers.ApproveRequestSerializer
        return serializers.RequestSerializer


class FixRequestViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = models.FixRequest.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return serializers.CreateFixRequestSerializer
        return serializers.FixRequestSerializer


class TransferRequestViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = models.TransferRequest.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return serializers.CreateTransferRequestSerializer
        return serializers.TransferRequestSerializer
