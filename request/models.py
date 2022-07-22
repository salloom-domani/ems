from django.db import models
from asset.models import Asset, Department

class Request(models.Model):
    type = models.CharField(max_length=50)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    approve_number = models.PositiveSmallIntegerField(default=0)

    def get_approve_level(self):
        ...

class TransferRequest(Request):
    from_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='+')
    to_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='+')

class FixRequest(Request):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    SEVERITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]

    severity = models.CharField(max_length=255, choices=SEVERITY_CHOICES, default=LOW)
    note = models.CharField(max_length=255)