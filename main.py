import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token=os.getenv("DISCORD_TOKEN")


bot=commands.Bot(command_prefix="!")

@bot.command(name="bday")
async def bday(ctx):
    await ctx.send("Happy Birthday")

@bot.event
async def on_command_error(ctx, error):
    print(error)



bot.run(token)
