from django.contrib import admin
from . import models


@admin.register(models.Request)
class RequestAdmin(admin.ModelAdmin):
    pass

@admin.register(models.FixRequest)
class FixRequestAdmin(admin.ModelAdmin):
    pass

@admin.register(models.TransferRequest)
class TransferRequestAdmin(admin.ModelAdmin):
    pass
