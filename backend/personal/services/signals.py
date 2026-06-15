# SPDX-License-Identifier: AGPL-3.0-or-later


from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@receiver(post_save, sender='personal.InboundMessageModel')
def notify_new_message(sender, instance, created, **kwargs):
    if kwargs.get('raw'):
        return

    if created:
        from personal.serializers import InboundMessageSerializer

        channel_layer = get_channel_layer()
        serializer = InboundMessageSerializer(instance)

        async_to_sync(channel_layer.group_send)(
            "inbox_updates",
            {
                "type": "inbox.message",
                "content": serializer.data
            }
        )