import discord
import search_csgoStash
import os
my_secret = os.environ['TOKEN']
csgostashweb = search_csgoStash.CSGOSTASH()

client = discord.Client()

#check when bot online
@client.event
async def on_ready():
  print(f'{client.user} is online')

@client.event
async def on_message(message): 
  # stops bot responding to itself
  if message.author == client.user:
      return  
  # converts message to all lower case - helps with bot readability
  message_content = message.content.lower()
  
  if message.content.startswith(f'$hello'):
    await message.channel.send('''Hello there! ''')


client.run('my_secret')
