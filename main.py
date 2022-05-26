print("                                                                      ")
print("░██████╗░██████╗░░█████╗░███╗░░██╗████████╗  ██╗░░██╗██╗░░░██╗██████╗░")
print("██╔════╝░██╔══██╗██╔══██╗████╗░██║╚══██╔══╝  ██║░░██║██║░░░██║██╔══██╗")
print("██║░░██╗░██████╔╝███████║██╔██╗██║░░░██║░░░  ███████║██║░░░██║██████╦╝")
print("██║░░╚██╗██╔══██╗██╔══██║██║╚████║░░░██║░░░  ██╔══██║██║░░░██║██╔══██╗")
print("╚██████╔╝██║░░██║██║░░██║██║░╚███║░░░██║░░░  ██║░░██║╚██████╔╝██████╦╝")
print("░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░  ╚═╝░░╚═╝░╚═════╝░╚═════╝░")
token = input("Bot token:")
config = input("Prefix:")
amount = input("Amount channel to spam:")
name = input("Name Spam:")
serverid = input("Server Id:")
import discord
from discord.ext import commands
from discord.utils import get
client = discord.Client()
names = name
bot = commands.Bot(command_prefix=config, cas_insentive=True, help_command=None)
text = "createchanel " + name + " in " + serverid
textr = "createrole " + name + " in " + serverid
@bot.command()
async def spamch(ctx):
    guild = ctx.message.guild
    for i in range(1, 500):
        print(text)
        channels = await guild.create_text_channel(name) 
@bot.command()
async def spamrole(ctx):
    guild = ctx.message.guild
    for i in range(1, 500):
        print(textr)
        await guild.create_role(name=names)
bot.run(token)
