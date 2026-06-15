# SPDX-License-Identifier: AGPL-3.0-or-later


import json
from channels.generic.websocket import AsyncWebsocketConsumer

class InboxConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "inbox_updates"

        # Connecting to the group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Quit from the group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # Getting the date from the Redis
    async def inbox_message(self, event):
        # Send JSON to the client (Vue)
        await self.send(text_data=json.dumps(event["content"]))