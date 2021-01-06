import discord
from discord.ext import commands
intents=discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents)
token = ''
@client.event
async def on_ready():
	print('logged in successfully!')
@client.command()
async def massdm(ctx, *, message):
    number = 0
	for guild in client.guilds:
		for member in guild.members:
			try:
                if member != ctx.author.id:
                    channel = await member.create_dm()
                    await channel.send(message)
                    await ctx.send(f':white_check_mark: Successfully dmed {member}!')
                    number +=1
			except:
				await ctx.send(f':x: Could not dm {member}')
    await ctx.send(f'Successfully finished and dmed {number} times')
@client.command()
async def servers(ctx):
    await ctx.send(f"I am currently in `{len(client.guilds)}` servers")
client.run(token)