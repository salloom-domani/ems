from email.policy import default
from rest_framework.serializers import ModelSerializer
from rest_framework import fields
from .models import Request, FixRequest, TransferRequest

class RequestSerializer(ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class ApproveRequestSerializer(ModelSerializer):
    class Meta:
        model = Request
        fields = ['approve_number']

class FixRequestSerializer(ModelSerializer):
    type = fields.CharField(read_only=True, default='fixrequest')
    class Meta:
        model = FixRequest
        fields = '__all__'

class TransferRequestSerializer(ModelSerializer):
    type = fields.CharField(read_only=True, default='transferrequest')
    class Meta:
        model = TransferRequest
        fields = '__all__'