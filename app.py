import os

import discord

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

BANNED_WORDS = [
    'shit',
    'piss',
    'fuck',
    'cunt',
    'cocksucker',
    'motherfucker',
    'tits',
]

@client.event
async def on_ready():
    for guild in client.guilds:
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

@client.event
async def on_message(message):
    if message.author.id != client.user.id:
        matches = {word for word in BANNED_WORDS if word in message.content}
        if matches:
            alert = f'{message.author.name}: {message.content} which includes the words {matches} {message.jump_url}'
            chan = discord.utils.get(message.guild.channels, name=os.getenv('ALERT_CHANNEL'))
            await chan.send(alert)

client.run(TOKEN)
