from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Notification
from request.models import FixRequest, TransferRequest
from request.serializers import FixRequestSerializer, TransferRequestSerializer

class ContentRelatedField(serializers.RelatedField):
    """
    A custom field to use for the `content_object` generic relationship.
    """

    def to_representation(self, value):
        """
        Serialize tagged objects to a simple textual representation.
        """
        if isinstance(value, FixRequest):
            serializer = FixRequestSerializer(value)
        elif isinstance(value, TransferRequest):
            serializer = TransferRequestSerializer(value)
        else:
            raise Exception('Unexpected type of content object')

        return serializer.data


class NotificationSerializer(ModelSerializer):
    content = ContentRelatedField(source='content_object', read_only=True)
    class Meta:
        model = Notification
        fields = ['id', 'user', 'content', 'note']
