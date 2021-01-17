import discord
from discord.ext import commands
import utils
import os.path
import json
from datetime import date

class Profile(commands.Cog):
    
    DATADIR = "Data/"

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        utils.ext_message("Profile")

    @commands.command()
    async def profile(self, ctx):
        author = ctx.author
        authorId = str(author.id)
        server = str(ctx.guild.id)
        serverDir = self.DATADIR+server+"/"
        authorDir = serverDir+authorId+".json"
        output = ""

        if os.path.isfile(authorDir):
            print("User exists, proceeding to open JSON file of user "+authorId)
            with open(authorDir) as json_file:

                data = json.load(json_file)

            #print(data)
            #print (data["Characters"]["test"]["CreationDate"])
            print("Loading user: "+data["UserData"]["Username"]+" (is admin? "+str(data["UserData"]["isAdmin"])+")")
            print("Sending profile info about user "+authorId)
            #output = "Username: "+str(data["UserData"]["Username"])+"\nAdmin? "+str(data["UserData"]["isAdmin"])+"\nUser creation date: "+str(data["UserData"]["CreationDate"])
            
            embed=discord.Embed(title=str(data["UserData"]["Username"]), description="", color=utils.random_color())
            if(data["UserData"]["isAdmin"]):
                embed.add_field(name="Admin?", value=str(data["UserData"]["isAdmin"]), inline=False)
            embed.add_field(name="User creation date", value=str(data["UserData"]["CreationDate"]), inline=False)

            #await ctx.send(embed = embed)
            await utils.send_message(ctx, embed)
            print("------")
            

    @commands.command()
    async def newCharacter(self, message, *args):
        author = message.author
        authorId = str(author.id)
        server = str(message.guild.id)
        charName = ""
        serverDir = self.DATADIR+server+"/"
        authorDir = serverDir+authorId+".json"
        today = str(date.today())

        #for arg in args:
            #charName = charName + " " + arg
        #print(charName)
        charName = args[0]

        if os.path.isfile(authorDir):
            print("User exists, proceeding to open JSON file of user "+authorId)
            
            #with open(authorDir, 'r') as f:
            #    dataList = [json.loads(line[7:]) for line in f]

            #for row in table:
            #    print(row)
            with open(authorDir) as json_file:

                data = json.load(json_file)

            #print(data)
            #print (data["Characters"]["test"]["CreationDate"])
            print("Loading user: "+data["UserData"]["Username"]+" (is admin? "+str(data["UserData"]["isAdmin"])+")")
            print("Creating character: \""+charName+"\"")

            print("------")

        else:
            print("User does not exist, proceeding to create JSON file for user "+authorId)
            
            userData = {
            "UserData": {
                "Username": author.name,
                "CreationDate": today,
                "isAdmin": False
                },
            "Characters": {
                charName: { 
                    "Name": charName,
                    "CreationDate": today,
                    "Lever": 1,
                    "Stats": {
                        "HP": 10
                        }
                    }
                }
            }
            #print(charData)

            if not os.path.exists(os.path.dirname(serverDir)):
                try:
                    print("Server does not exist, proceeding to create folder for server "+server)
                    
                    os.makedirs(os.path.dirname(serverDir))
                except OSError as exc: # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise
            f = open(authorDir, "w")
            f.write(json.dumps(userData))
            f.close()
            
            print("------")


def setup(bot):
    bot.add_cog(Profile(bot))