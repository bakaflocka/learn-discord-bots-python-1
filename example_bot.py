#my script was created in the Raspberry Pi OS, but should work with any OS with Python installed
#paste the script below into your text editor and save as a .py file - comments such as this can be removed for cleaner code
#when the script is running correctly, your Discord bot will log into the Discord server, as verified in the server's users list
#refer to the read me for this repository for more help if needed

import discord
#imports library which allows your discord bot to communicate with discord, using definitions and commands below

client = discord.Client()
#creates instance of a client, which is our connection to Discord

@client.event
async def on_ready():
	print('What it do, just logged in as {0.user}'.format(client))
#registers event. Library is asynchronous, we do things in a "callback" style manner
#the on_ready event is called when the bot finishes logging in 
	
#below, on_message event is called when the bot has received a message
#message.author == client.user is used to ignore messages from the bot itself
@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith('!hello'):
		await message.channel.send('Hello!')
	if message.content.startswith('!findgod'):
		await message.channel.send('Skete Davidson says no.')
#if a message in the Discord starts with '!hello', then bot sends back message 'Hello!' in channel

client.run('YOUR DISCORD BOT TOKEN')
#paste your Discord Bot's token above. Leave the opening ' and closing ' for syntax purposes
#friendly reminder to never share your bot's token
