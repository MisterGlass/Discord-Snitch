import os

import discord

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

f = open(os.getenv('WORD_LIST'), 'r+')
BANNED_WORDS = [line.strip().lower() for line in f.readlines()]
f.close()

IGNORED_CHANNELS = os.getenv('IGNORED_CHANNELS').split(',')

@client.event
async def on_ready():
    for guild in client.guilds:
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

@client.event
async def on_message(message):
    if message.author.id != client.user.id and message.channel.name not in IGNORED_CHANNELS:
        matches = {word for word in BANNED_WORDS if word in message.content.lower()}
        if matches:
            alert = f'{message.author.name}: {message.content} which includes the words {matches} {message.jump_url}'
            chan = discord.utils.get(message.guild.channels, name=os.getenv('ALERT_CHANNEL'))
            await chan.send(alert)

client.run(TOKEN)
