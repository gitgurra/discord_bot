import discord
import time
from members import MemberObj

TOKEN = "NjgxNDg2ODE0ODU4NTc2MDY0.XlPLTg.twq4novIHJuZ3fYJXknCjkryKqI"

client = discord.Client()
member_list = {}

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('!mystats'):
        temp = member_list[message.author.name].get_active_time()
        msg = ('{0.author.mention} has spent %s seconds in voice chat' % temp).format(message)
        await message.channel.send(msg)

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!smr'):
        await message.channel.send('Kul.')

@client.event
async def on_voice_state_update(member, before, after):
    try:
        member_list[member.name].state_change(member.voice.channel)
    except:
        member_list[member.name].state_change(None)

    print('Someone did something in a voice channel')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    for guild in client.guilds:
        for member in guild.members:
            if member != client.user:
                member_list[member.name] = MemberObj(member.name)
    print('Stattracker initialized')
    print('-------')

client.run(TOKEN)
