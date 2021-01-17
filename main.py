import os
import json
import discord
from discord.ext import commands
import utils

with open("./config.json", "r") as configjsonFile:
    configData = json.load(configjsonFile)
    TOKEN = configData["DISCORD_TOKEN"]
    PREFIX = configData["BOT_PREFIX"]
    DESCRIPTION = configData["BOT_DESCRIPTION"]
    EXT_FOLDER = configData["EXTENSIONS_FOLDER"]

extensions = [EXT_FOLDER+".profile"]

bot = commands.Bot(command_prefix=PREFIX, description=DESCRIPTION)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_command_error(ctx, error):
    #if isinstance(error, CommandNotFound):
    print(str(error)+" (server id: "+str(ctx.guild.id)+", user id: "+str(ctx.author.id)+")  ")
    await ctx.send("Invalid command \""+ctx.message.content[1:]+"\"")
    print("------")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def test(ctx):
    print(bot.user.name)
    print(bot.user.id)
    await ctx.send('test')

@bot.command()
async def embed(ctx):
    embed=discord.Embed(title="Tile", description="Desc", color=0x00ff00)
    embed.add_field(name="Fiel1", value="hi", inline=False)
    embed.add_field(name="Field2", value="hi2", inline=False)
    await ctx.send(embed=embed)

if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run(TOKEN)