from rest_framework.serializers import ModelSerializer
from .models import Request, FixRequest, TransferRequest

class RequestSerializer(ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class FixRequestSerializer(ModelSerializer):
    class Meta:
        model = FixRequest
        fields = '__all__'

class TransferRequestSerializer(ModelSerializer):
    class Meta:
        model = TransferRequest
        fields = '__all__'