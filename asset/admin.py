from django.contrib import admin
from . import models


@admin.register(models.Asset)
class AssetAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass
