import os
import json
import discord
from discord.ext import commands

def extMessage(extName):
    print('Extension '+extName+' loaded')
    print('------')

async def sendMessage(ctx, s):
    await ctx.send(s)
    print("Message sent succesfully")
    

