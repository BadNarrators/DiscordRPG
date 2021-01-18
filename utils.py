import os
import json
import discord
from discord.ext import commands
import random

def ext_message(extName):
    print('Extension '+extName+' loaded')
    print('------')

async def send_message(ctx, s):
    if(type(s)==discord.embeds.Embed):
        await ctx.send(embed = s)
    else:
        await ctx.send(s)
        
    print("Message sent succesfully")
    
def random_color():
    color = random.randint(0, 0xffffff)
    return color

#not working, have to investigate on old js code to check
async def npc_message(ctx, npc, s):
    embed=discord.Embed(title="test", description="test", color=random_color())
    embed.set_author(name="Test")
    await send_message(ctx, embed)