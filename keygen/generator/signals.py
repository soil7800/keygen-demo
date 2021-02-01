from .models import GeneratedKey
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def change_key(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
            "online_users",
            {
                "type": "new.key",
                "key": str(instance),
                "last_updated": str(int(instance.updated.timestamp()*1000)),
            },
        )