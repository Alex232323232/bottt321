#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sasha
#
# Created:     28.03.2021
# Copyright:   (c) sasha 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import diskord
from discord.ext import commands

client = commands.Bot( command_prefix = "." )
# .hello

@client.event

async def on_ready():
    print("Bot connected")

@client.command( pass_context = True )

async def hello( ctx ):
    await ctx.send( "Hello, Gay!")

# Connect

token = open( "token.txt" , "r").readline()

client.run( token )