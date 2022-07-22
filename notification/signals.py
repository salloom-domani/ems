from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification
from request.models import FixRequest, TransferRequest

@receiver(post_save, sender=FixRequest)
@receiver(post_save, sender=TransferRequest)
def create_notification_for_new_request(sender, instance, **kwargs):
    if kwargs['created']:
        request_type = instance.type
        asset = instance.asset
        print(sender)
        print(instance)
        user = asset.reporter.user
        note = ''
        if request_type == 'fixrequest':
            note = f'We have to fix ({asset.name}) asset with {asset.severity} severity'
        elif request_type == 'transferrequest':
            from_department = instance.from_department
            to_department = instance.to_department
            note = f'We have to transfer ({asset.name}) asset from {from_department} department to {to_department} department'
        Notification.objects.create(user=user, content_object=instance, note=note)