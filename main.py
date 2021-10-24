import os
import asyncio
import random
import discord
from discord.ext import commands
import helper_functions
import keep_alive
from helper_functions import scareface
from helper_functions import offset_list
from helper_functions import mentions

"""Denna modul är main modulen som faktiskt hanterar discord delen av boten"""


token = os.environ['TOKEN']
bot = commands.Bot(command_prefix='$')


@bot.command()
async def ping(ctx):
    """Kommando som visar bottens svarstid"""
    embed = discord.Embed(
        title="Pong!",
        description=("Det Kongliga Drifveriet svarar vanligtvis snabbare än ljusets hastighet, "
                    "men för att ~~nØllans~~ ettans synapser skall hänga med "
                    f"har det Kongliga Drifveriet beslutat att svara på {round(bot.latency*1000)} millisekunder!")
    )
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/572159063505371137/900800963651199086/drifveriet.png")
    await ctx.send(embed=embed)


@bot.event
async def on_ready():
    """Skriver ut att botten är online"""
    print("Drifvare online.")


@bot.event
async def on_message(message):
    """Hanterar meddelander reaktioner som triggar boten"""
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
            await message.edit(content="\n".join(
                [random.choice(offset_list) * " " + x for x in scareface.split("\n")]))
            await asyncio.sleep(random.choice([0, 0, 0.25, 0.5, 1]))
        await message.edit(content=scareface)
        mentions = 0

    elif mention in message.content:
        await message.channel.send("Drifveriet ser ~~nØllan~~ ettan.")

    elif "en hel del" in message.content.lower():
        await message.channel.send("mmmmMMM**PENGAR**")

    elif any(x in message.content.lower() for x in ("pit bull", "pitbull")):
        await message.channel.send("dale")

    elif "betong" in message.content.lower():
        await message.channel.send(
            ("Bakom 30 meter betong, 5 blyinfattade pansardörrar och 60 rader pythonkod har det"
             " Kongliga Drifveriet observerat ~~nØllans~~ ettans discordkunskaper."
             " Det har *inte* gått bra. **Inte så bra alls!!!**"
             " ***Att säga att ettan är bra på discord är lite som att tro att drifveriet inte kan höra vad du tänker just nu.***"
             )
        )

    elif random.randint(0, 500) == 420:
        await helper_functions.jubla(message)

    await bot.process_commands(message)


keep_alive.keep_alive()
bot.run(token)
