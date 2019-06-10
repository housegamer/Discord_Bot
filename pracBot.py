import discord
import sys


client = discord.Client()
token = open("token.txt", "r").read()

@client.event #event decorator/wrapper
async def on_ready():
	print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
	print(f'{message.channel}: {message.author}: {message.author.name}: {message.content}')
	prac_guild = client.get_guild(506981113487687682)

	if "pracbot.member_count()" == message.content.lower():
		await message.channel.send(f"```py\n{prac_guild.member_count}```")

	elif 'pracbot.logout()' == message.content.lower():
		await client.close()
		#sys.exti()

	elif "pracbot.community_report()" == message.content.lower():
		online = 0
		idle = 0
		offline = 0

		for m in prac_guild.members:
			if str(m.status) == 'online':
				online += 1
			if str(m.status) == 'offline':
				offline +=1
			else:
				idle +=1

		await message.channel.send(f" Online : {online}.\nIdle/busy/dnd: {idle}. \nOffline: {offline}")


client.run(token)