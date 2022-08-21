import os
import asyncio
import time

from pyrogram import Client

import utils
# import settings

class Answer:
    pass

class Chat:
    pass

class Telegram:
    def __init__(self, loop):
        self.api_id = int(os.environ.get("API_ID"))
        self.api_hash = str(os.environ.get("API_HASH"))
        self.session_name = str(os.environ.get("SESSION_NAME"))
        self.bot_token = str(os.environ.get("BOT_TOKEN"))
        self.chat_id = str(os.environ.get("CHAT_ID"))
        self.workers = 2

        self.client: Client

        self.event_loop = loop
        self.autodeleting = None

    async def create_session(self):

        self.client = Client(
            self.session_name,
            api_id=self.api_id,
            api_hash=self.api_hash,
            workers=self.workers,
            workdir='sessions/'
        )

        # self.autodeleting

        instace = self

        @self.client.on_message()
        def message_handler(self, message):
            pass

        @self.client.on_disconnect()
        def disconnect_handler(self, message=None):
            while not self.is_connected:
                time.sleep(10)

                if self.is_connected:
                    break

                try:
                    self.connect()
                except:
                    pass

        @self.client.on_deleted_messages()
        def deleted_messages_handler(self, message=None):
            pass

        @self.client.on_user_status()
        def user_status_handler(self, message=None):
            pass

    async def start_session(self):
        if self.client:
            self.client.start()