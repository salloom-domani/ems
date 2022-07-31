from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from .models import Asset, Department, Employee


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = "__all__"


class SimpleAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ["id", "name"]


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class SimpleDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ["id", "name"]


class CreateEmployeeSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    user = UserCreateSerializer()

    class Meta:
        model = Employee
        fields = ["first_name", "last_name", "department", "is_admin", "user"]

    
    def save(self, **kwargs):
        user = self.validated_data["user"]
        first_name = self.validated_data["first_name"]
        last_name = self.validated_data["last_name"]
        name = f'{first_name} {last_name}'
        is_admin = self.validated_data["is_admin"]
        department = self.validated_data["department"]

        User = get_user_model()
        user = User.objects.create(**user, is_staff=is_admin, first_name=first_name, last_name=last_name)

        return Employee.objects.create(
            name=name, department=department, is_admin=is_admin, user=user
        )


class EmployeeSerializer(serializers.ModelSerializer):
    my_departments = SimpleDepartmentSerializer(many=True, read_only=True)
    assets = SimpleAssetSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = "__all__"
