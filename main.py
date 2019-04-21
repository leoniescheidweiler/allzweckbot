from telethon.sync import TelegramClient
from telethon import events

import json
import asyncio
import random
import datetime
import pytz

tz = pytz.timezone('Europe/Berlin')

from functions import allesdreck
from functions import kolloquium

async def main():
    with open('credentials.json', 'r') as file:
        credentials = json.load(file)
    with open('group_info.json', 'r') as file:
        group_info = json.load(file)

    client = TelegramClient(
            credentials['session_name'],
            credentials['api_id'],
            credentials['api_token'])
    await client.start(bot_token = credentials['bot_token'])

    me = await client.get_me()
    print('Logged in as ' + me.username + '.')

    # Do once to get channel
    #@client.on(events.NewMessage())
    #async def get_group(event):
    #    group_chat = await client.get_entity(event.message.to_id.chat_id)
    #    print(group_chat.stringify())
    #    for user in await client.get_participants(group_chat):
    #        await client.get_entity(user)
    #        print(user)

    group_chat = await client.get_entity(group_info["group_id"])

    # FUNCTIONS

    async def get_allesdreck():
        while True:
            hour = int(datetime.datetime.now(tz).hour)
            minute = int(datetime.datetime.now(tz).minute)
            weekday = int(datetime.datetime.now(tz).weekday())
            if (hour==11 and minute==0):
                if weekday < 5:
                    await asyncio.sleep(4)
                    await client.send_message(group_chat, allesdreck.allesdreck())
                    await asyncio.sleep(60*60*23*1/60*55)
                else:
                    await asyncio.sleep(60*60*23*1/60*55)
            await asyncio.sleep(20)
    get_allesdreck = loop.create_task(get_allesdreck())

    async def get_kolloquium():
        while True:
            hour = int(datetime.datetime.now(tz).hour)
            minute = int(datetime.datetime.now(tz).minute)
            weekday = int(datetime.datetime.now(tz).weekday())
            if (weekday == 3 and hour==20 and minute==0):
                await asyncio.sleep(4)
                await client.send_message(group_chat, kolloquium.kolloquium())
                await asyncio.sleep(60*60*24*7-100)
            await asyncio.sleep(20)
    get_kolloquium = loop.create_task(get_kolloquium())

    await get_allesdreck
    await get_kolloquium

    await client.run_until_disconnected()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
