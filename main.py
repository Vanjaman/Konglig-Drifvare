import os
import asyncio
import discord
import helper_functions
from helper_functions import scareface
from helper_functions import offset_list
from helper_functions import mentions
from discord.ext import commands
import random

import keep_alive

token = os.environ['TOKEN']
bot = commands.Bot(command_prefix='$')
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def ping(ctx):
    embed = discord.Embed(title="Pong!",description=f"Drifveriet svarar snabbare än ljuset hastighet, vilket avrundas uppåt till {round(bot.latency*1000,4)} ms")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/572159063505371137/900800963651199086/drifveriet.png")
    await ctx.send(embed=embed)


@bot.event
async def on_ready():
    print("Drifvare online.")

@bot.event
async def on_message(message):
    global mentions
    if message.author == bot.user:
        return
    mention = f'<@!{bot.user.id}>'

    if mention in message.content:
        mentions += 1
    else:
        mentions = 0

    if mentions == 3 or message.content.count(mention) == 3:
        message = await message.channel.send(scareface)
        for _ in range(4):
            await message.edit(content="\n".join([random.choice(offset_list) * " " + x for x in scareface.split("\n")]))
            await asyncio.sleep(random.choice([0, 0, 0.25, 0.5, 1]))
        await message.edit(content=scareface)
        mentions = 0

    elif mention in message.content:
        await message.channel.send("Drifveriet ser ~~nØllan~~ ettan.")

    elif message.content.startswith("ping"):
        await message.channel.send("pong")

    elif "en hel del" in message.content.lower():
        await message.channel.send("mmmmMMM**PENGAR**")

    elif any(x in message.content.lower() for x in ("pit bull", "pitbull")):
        await message.channel.send("dale")

    elif "betong" in message.content.lower():
        await message.channel.send("Bakom 30 meter betong, 4 blyinfattade pansardörrar och 61 rader pythonkod har det Kongliga Drifveriet observerat ~~nøllans~~ ettans discordkunskaper. Det har *inte* gått bra. **Inte så bra alls!!!** ***Att säga att ettan är bra på discord är lite som att tro att drifveriet inte kan höra vad du tänker just nu.***")

    elif random.randint(0, 500) == 420:
        await helper_functions.jubla(message)

    await bot.process_commands(message)




keep_alive.keep_alive()
bot.run(token)
