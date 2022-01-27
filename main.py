import discord #importing discord library
import os #importing the token library

client = discord.Client() #define client as a discord bot

@client.event #action on interaction with the bot
async def on_ready():
  print('We logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))
