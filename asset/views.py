from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers


class AssetViewSet(ModelViewSet):
    serializer_class = serializers.AssetSerializer
    queryset = models.Asset.objects.all()

class DepartmentViewSet(ModelViewSet):
    serializer_class = serializers.DepartmentSerializer
    queryset = models.Department.objects.all()

class EmployeeViewSet(ModelViewSet):
    queryset = models.Employee.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.CreateEmployeeSerializer
        return serializers.EmployeeSerializer