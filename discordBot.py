import discord
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
# client = discord.Client()

@client.event
async def on_ready():
    print("Duhh, The LAZY Bot is here")

@client.event
async def on_message(message):
    if(message.author == client.user):
        return
    if (str(message.author) == "highafboysss#0831"):
        if (str(message.content).lower() == "hello" or str(message.content).lower() == "hi" or str(
                message.content).lower() == "hey"):
            await message.add_reaction("\U0001F44B")
            await message.channel.send("Welcome!! GOD")
    elif (str(message.content).lower() == "hello" or str(message.content).lower() == "hi" or str(message.content).lower() == "hey"):
        await message.add_reaction("\U0001F44B")
        await message.channel.send("Welcome!! You lazy fuck")

@client.event
async def on_reaction_add(reaction,user):
    await reaction.message.channel.send(str(user) + " reacted with " + reaction.emoji)

@client.event
async def on_message_edit(before,after):
    await before.channel.send(str(before.author) + " edited a message.\nBefore: " + before.content + "\nAfter: " + after.content)

@client.event
async def on_raw_reaction_add(payload):
    payload_message_id = payload.message_id
    target_message_id = 859801658955661393
    guild_id = payload.guild_id
    guild = client.get_guild(guild_id)
    if payload_message_id == target_message_id:
        print(payload.emoji.name)
        if payload.emoji.name == "😃":
            role = discord.utils.get(guild.roles, name="Happy")
            await payload.member.add_roles(role)
        elif payload.emoji.name == "😭":
            role = discord.utils.get(guild.roles, name="Sad")
            await payload.member.add_roles(role)
        elif payload.emoji.name == "😎":
            role = discord.utils.get(guild.roles, name="Cool")
            await payload.member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):
    payload_message_id = payload.message_id
    target_message_id = 859801658955661393
    guild_id = payload.guild_id
    guild = client.get_guild(guild_id)
    if payload_message_id == target_message_id:
        member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
        if payload.emoji.name == "😃":
            role = discord.utils.get(guild.roles, name="Happy")
            await member.remove_roles(role)
        elif payload.emoji.name == "😭":
            role = discord.utils.get(guild.roles, name="Sad")
            await member.remove_roles(role)
        elif payload.emoji.name == "😎":
            role = discord.utils.get(guild.roles, name="Cool")
            await member.remove_roles(role)

client.run('TOKEN')
