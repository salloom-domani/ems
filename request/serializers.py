from rest_framework import serializers
from rest_framework import fields
from .models import Request, FixRequest, TransferRequest

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class ApproveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['approve_number']

class FixRequestSerializer(serializers.ModelSerializer):
    type = fields.CharField(read_only=True, default='fixrequest')
    class Meta:
        model = FixRequest
        fields = '__all__'

class CreateFixRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixRequest
        fields = ['asset', 'severity', 'note']

    def create(self, validated_data):
        return FixRequest.objects.create(**validated_data, type='fixrequest')


class TransferRequestSerializer(serializers.ModelSerializer):
    type = fields.CharField(read_only=True, default='transferrequest')
    class Meta:
        model = TransferRequest
        fields = '__all__'

class CreateTransferRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferRequest
        fields = ['asset', 'from_department', 'to_department']

    def create(self, validated_data):
        return TransferRequest.objects.create(**validated_data, type='transferrequest')

    def validate(self, data):
        if data['from_department'] == data['to_department']:
            raise serializers.ValidationError("Cannot transfer asset to the same department.")
        return data