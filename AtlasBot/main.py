import discord
import os
import external_f as ext
from dotenv import load_dotenv
import requests
import json

my_secret = os.environ['TOKEN']

intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print("///Ready///")
  print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!hello'):
    await message.channel.send('Hello!')

  elif message.content.startswith('!homework'):
    # Extract the text following the command
    query = message.content[len('!Homework '):].strip()
    if query:  # Ensure there is a query
      response = ext.call_gpt_api(query)
      await message.channel.send(response)
    else:
      await message.channel.send('Please provide a query after "!Homework".')

  elif message.content.startswith('!help'):
    help_message = ('Commands:\n'
                    '!hello - Say hello\n'
                    '!homework <query> - Ask about your homework using GPT-4\n'
                    '!help - Show this help message')
    await message.channel.send(help_message)
  elif message.content.startswith('!whoami'):
    notice = (
        'I am Atlas version 0.0.1, I am currently utilizing GPT-3.5 Turbo '
        'for responeses\n')
    await message.channel.send(notice)


client.run(my_secret)
#Add additional functionality to perform youtube music searches
#Track interactions to gage userbase
