from rest_framework.serializers import ModelSerializer
from .models import Asset, Department, Employee

class AssetSerializer(ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class SimpleAssetSerializer(ModelSerializer):
    class Meta:
        model = Asset
        fields = ['id', 'name']

class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class SimpleDepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class EmployeeSerializer(ModelSerializer):
    my_departments = SimpleDepartmentSerializer(many=True, read_only=True)
    assets = SimpleAssetSerializer(many=True, read_only=True)
    class Meta:
        model = Employee
        fields = '__all__'