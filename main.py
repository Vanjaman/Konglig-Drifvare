import os
import asyncio
import discord
import random

import keep_alive

token = os.environ['TOKEN']
client = discord.Client()

global mentions
mentions = 0
offset_list = [0, 0, 0, 0, 0, 0, 0, 0, 7, 12, 15]
scareface = "⠀⠀⠀⢠⠣⡑⡕⡱⡸⡀⡢⡂⢨⠀⡌\n⠀⠀⠀⡕⢅⠕⢘⢜⠰⣱⢱⢱⢕⢵⠰⡱⡱⢘⡄⡎⠌⡀\n⠀⠀⠱⡸⡸⡨⢸⢸⢈⢮⡪⣣⣣⡣⡇⣫⡺⡸⡜⡎⡢\n⠀⠀⢱⢱⠵⢹⢸⢼⡐⡵⣝⢮⢖⢯⡪⡲⡝⠕⣝⢮⢪⢀\n⢀⠂⡮⠁⠐⠀⡀⡀⠑⢝⢮⣳⣫⢳⡙⠐⠀⡠⡀⠀⠑\n⢠⠣⠐⠀    ⭕     ⠀⢪⢺⣪⢣⠀⡀ ⭕   .⠈⡈⠀⡀\n⠐⡝⣕⢄⡀⠑⢙⠉⠁⡠⡣⢯⡪⣇⢇⢀⠀⠡⠁⠁⡠⡢⠡\n⠀⢑⢕⢧⣣⢐⡄⣄⡍⡎⡮⣳⢽⡸⡸⡊⣧⣢⠀⣕⠜⡌⠌\n⠀⠀⠌⡪⡪⠳⣝⢞⡆⡇⡣⡯⣞⢜⡜⡄⡧⡗⡇⠣⡃⡂\n⠀⠀⠀⠨⢊⢜⢜⣝⣪⢪⠌⢩⢪⢃⢱⣱⢹⢪⢪⠊\n  ⠀⠀⠐⠡⡑⠜⢎⢗⢕⢘⢜⢜⢜⠜⠕⠡⠡⡈\n⠀⠀⠀⠀⠀⠁⡢⢀⠈⠨⣂⡐⢅⢕⢐⠁⠡⠡⢁\n⠀⠀⠀⠀⠀⠀⢈⠢⠀⡀⡐⡍⢪⢘⠀⠀⠡⡑⡀\n⠀⠀⠀⠀⠀⠀⠀⠨⢂⠀⠌⠘⢜⠘⠀⢌⠰⡈\n⠀⠀⠀⠀⠀⠀⠀⠀⢑⢸⢌⢖⢠⢀⠪⡂\n\n                    L̶̡̛͙͍̜̬̬̣̝͇̼̤̤̣̥͋̽͒͑̄̿̐̋̇͂̃̀o̴̡̨̗͔̜̟̬̤̭̤̙̥̘͋̅͜ͅo̷̦̠̮̹̼̥͎͇̲̰͙͐͌̎̓̈́͂̌̇͜k̵̡̡̢̠̬̜͈̭̻̘̮̼̱̱͍̐̿̈́̅͊͐͊͐̚̚͘͠͠ ̶͓̪̯̗̒̊̃̿͌̈́̂͗͂͝͠b̴̨͇͍͒̀̈͝ͅẹ̴̬̉̍̄͘͠h̴̟͓̻͔͝į̶̧̧̤̦͓͕̑͝n̸͎̻̬̊̄̆̈́̒̃d̸̡̡͓̼͉͈̮͈͖̤͔̎̂͑̍̔̅͋̀̃́̒̕͜ ̴̼̘͙͉̺̮̭̭͍̰̍͗̓̐͂͂͒͒͠y̴̢͖̺̩̗̖̰͙͕̜͖̹͕͒̄ͅǫ̶̢͕̳͖̣͈̰̖̜̙̬̓͌̂͑̉̅̾͆̀̊͜ṵ̵͕͔͙͖̣̾̄̀̃"


@client.event
async def on_ready():
    print("Drifveriet ser --nøllan-- ettan.")


@client.event
async def on_message(message):
    global mentions
    if message.author == client.user:
        return
    mention = f'<@!{client.user.id}>'

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
        await message.channel.send("Bakom 30 meter betong, 4 blyinfattade pansardörrar och 61 rader pythonkod har det Kongliga Drifveriet observerat ~~nøllans~~ ettans discordkunskaper. Det har inte gått bra. Inte så bra alls. Att säga att ettan är bra på discord är lite som att tro att drifveriet inte kan höra vad du tänker just nu.")

    elif random.randint(0, 500) == 420:
        await message.channel.send("**DUNK**")
        await asyncio.sleep(2)
        await message.channel.send("**DUNK**")
        await asyncio.sleep(2)
        await message.channel.send("**DUNK**")
        await asyncio.sleep(2)
        message = await message.channel.send("**jjjjj**")
        await asyncio.sleep(1)
        await message.edit(content="**jjjjjuuuuuuuuuuuu**")
        await asyncio.sleep(1)
        await message.edit(content="**jjjjjuuuuuuuuuuuuuuuuuu**")
        await asyncio.sleep(1)
        await message.edit(content="**jjjjjuuuuuuuuuuuuuuuuuubbbllll**")
        await asyncio.sleep(1)
        await message.edit(content="**jjjjjuuuuuuuuuuuuuuuuuubbbllllaaaaaaaaaaaaaaa**")
        await asyncio.sleep(1)
        await message.edit(content="**jjjjjuuuuuuuuuuuuuuuuuubbbllllaaaaaaaaaaaaaaaaaaaaaaaaaa**")
        await asyncio.sleep(1)
        await message.edit(content="**jjjjjuuuuuuuuuuuuuuuuuubbbllllaaaaaaaaaaaaaaaaaaaaaaaaaa!!!!!1!**")


keep_alive.keep_alive()
client.run(token)