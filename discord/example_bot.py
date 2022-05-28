import discord
import logging

logging.basicConfig(level=logging.INFO)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('OTc2NjgyODMyNDM5MTQ4NTU1.GXoCtB.Cc0EKVQDxFa_pQxoPGhcE_kcr0rUKaNSQCj6nE')
