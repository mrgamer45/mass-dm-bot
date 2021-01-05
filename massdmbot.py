import discord
from discord.ext import commands
intents=discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents)
token = 'NzgwNTI0MTg1NDgyNTU5NTA5.X7wVyw.Jz4R3JHOgtsGSPUdvCP8hP31Ykw'
@client.event
async def on_ready():
	print('logged in successfully!')
@client.command()
async def massdm(ctx, *, message):
	for guild in client.guilds:
		for member in guild.members:
			try:
                if member != ctx.author.id:
                    channel = await member.create_dm()
                    await channel.send(message)
                    await ctx.send(f'Successfully dmed {member}!')
			except:
				await ctx.send(f'Could not dm {member}')
client.run(token)