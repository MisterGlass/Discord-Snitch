import logging
import os

import discord

# Hardcoded variables
REMOVED_CHARS = '_*'

# Pull & expand settings
TOKEN = os.getenv('DISCORD_TOKEN')
LOG_FILE = os.getenv('LOG_FILE')

client = discord.Client()

f = open(os.getenv('WORD_LIST', 'words'), 'r+')
BANNED_WORDS = [line.strip().lower() for line in f.readlines()]
f.close()

IGNORED_CHANNELS = os.getenv('IGNORED_CHANNELS', '').split(',')
IGNORED_ROLES = os.getenv('IGNORED_ROLES', '').split(',')

# Setup logger
log_settings = {
    'level': logging.WARN,
    'format': '%(asctime)s %(message)s',
}
if LOG_FILE:
    log_settings['filename'] = LOG_FILE
    log_settings['encoding'] = 'utf-8'
logging.basicConfig(**log_settings)


# Message handler
async def _process_message(author, content, guild, channel, jump_url):
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
        logging.warning(alert)
        await chan.send(alert)


# Initialize
@client.event
async def on_ready():
    for guild in client.guilds:
        logging.warning(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )


# Listen to new messages
@client.event
async def on_message(message):
    await _process_message(
        message.author,
        message.content,
        message.guild,
        message.channel,
        message.jump_url,
    )


# Listen to raw edits - regular could miss edits of messages we don't have cached
@client.event
async def on_raw_message_edit(payload):
    if payload.data['content'] and payload.cached_message:
        await _process_message(
            payload.cached_message.author,
            payload.data['content'],
            payload.cached_message.guild,
            payload.cached_message.channel,
            payload.cached_message.jump_url,
        )

client.run(TOKEN)
