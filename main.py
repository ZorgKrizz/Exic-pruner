#dont skid
import discord
import os
import colorama
from colorama import Fore
from discord.ext import commands
os.system("clear")


client = discord.Client()

client= commands.Bot(command_prefix='>', self_bot=True)

TOKEN = input(f"{Fore.MAGENTA}>  {Fore.WHITE}Token : ")

print(f'''
{Fore.GREEN}
███████╗██╗░░██╗██╗░█████╗░  
██╔════╝╚██╗██╔╝██║██╔══██╗
█████╗░░░╚███╔╝░██║██║░░╚═╝
██╔══╝░░░██╔██╗░██║██║░░██╗
███████╗██╔╝╚██╗██║╚█████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░╚════╝░

[ + ] Team Exic
[ + ] Oxydize/Krizz
[ + ] Dont Skid
''')


@client.command()
async def Prune(ctx):
  await ctx.message.delete()
  print(f'''{Fore.MAGENTA}[ + ] Succesfully Pruned''')
  await ctx.send("**Pruned | ``Exic Pruner``**")
  await ctx.guild.prune_members(days=1, compute_prune_count=False, roles=ctx.guild.roles, reason = "Exic Pruner | Pruned")


client.run(TOKEN, bot=False)
