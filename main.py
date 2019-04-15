from telethon.sync import TelegramClient
from telethon import events

import json
import asyncio
import random
import datetime

async def main():
    with open('credentials.json', 'r') as file:
        credentials = json.load(file)
    client = TelegramClient(
            credentials['session_name'],
            credentials['api_id'],
            credentials['api_token'])
    await client.start(bot_token = credentials['bot_token'])

    me = await client.get_me()
    print('Logged in as ' + me.username + '.')

    await client.run_until_disconnected()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
