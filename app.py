import os

import discord

REMOVED_CHARS = '_*'

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

f = open(os.getenv('WORD_LIST', 'words'), 'r+')
BANNED_WORDS = [line.strip().lower() for line in f.readlines()]
f.close()

IGNORED_CHANNELS = os.getenv('IGNORED_CHANNELS', '').split(',')
IGNORED_ROLES = os.getenv('IGNORED_ROLES', '').split(',')

async def process_message(author, content, guild, channel, jump_url):
    if author.id == client.user.id:
        return

    if channel.name in IGNORED_CHANNELS:
        return

    for role in author.roles:
        if role.name in IGNORED_ROLES:
            return

    text = content.lower()
    for char in REMOVED_CHARS:
        text = text.replace(char, '')

    matches = {word for word in BANNED_WORDS if word in text}
    if matches:
        alert = f'{author.name}: {content} which includes the words {matches} {jump_url}'
        chan = discord.utils.get(
            guild.channels, name=os.getenv('ALERT_CHANNEL'))
        await chan.send(alert)


@client.event
async def on_ready():
    for guild in client.guilds:
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )


@client.event
async def on_message(message):
    await process_message(
        message.author,
        message.content,
        message.guild,
        message.channel,
        message.jump_url,
    )


@client.event
async def on_raw_message_edit(payload):
    if payload.data['content'] and payload.cached_message:
        await process_message(
            payload.cached_message.author,
            payload.data['content'],
            payload.cached_message.guild,
            payload.cached_message.channel,
            payload.cached_message.jump_url,
        )

client.run(TOKEN)
