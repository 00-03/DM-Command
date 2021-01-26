import discord
form discord.ext import commands
import asyncio


TOKEN = 'token goes here'
bot = commands.Bot(command_prefix='/')
intents = discord.Intents.all()

@client.event()
async def on_ready():
    print('Online')



@client.command()
async def dm(ctx, *, message):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.send(message)
                print(f"{user.name} has recieved the message.")
            except:
                print(f"{user.name} has NOT recieved the message.")
        print("Action Completed: Mass DM")



    
bot.login(TOKEN)








