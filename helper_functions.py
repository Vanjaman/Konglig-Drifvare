import asyncio

global mentions
mentions = 0
jubla_list = [
    "**jjjjjuuuuuuuuuuuu**",
    "**jjjjjuuuuuuuuuuuu**",
    "**jjjjjuuuuuuuuuuuuuuuuuubbbllll**",
    "**jjjjjuuuuuuuuuuuuuuuuuubbbllllaaaaaaaaaaaaaaa**",
    "**jjjjjuuuuuuuuuuuuuuuuuubbbllllaaaaaaaaaaaaaaaaaaaaaaaaaa**",
    "**jjjjjuuuuuuuuuuuuuuuuuubbbllllaaaaaaaaaaaaaaaaaaaaaaaaaa!!!!!!**"
]
offset_list = [0, 0, 0, 0, 0, 0, 0, 0, 7, 12, 15]
scareface = \
    "⠀⠀⠀⢠⠣⡑⡕⡱⡸⡀⡢⡂⢨⠀⡌\n" \
    "⠀⠀⠀⡕⢅⠕⢘⢜⠰⣱⢱⢱⢕⢵⠰⡱⡱⢘⡄⡎⠌⡀\n" \
    "⠀⠀⠱⡸⡸⡨⢸⢸⢈⢮⡪⣣⣣⡣⡇⣫⡺⡸⡜⡎⡢\n" \
    "⠀⠀⢱⢱⠵⢹⢸⢼⡐⡵⣝⢮⢖⢯⡪⡲⡝⠕⣝⢮⢪⢀\n" \
    "⢀⠂⡮⠁⠐⠀⡀⡀⠑⢝⢮⣳⣫⢳⡙⠐⠀⡠⡀⠀⠑\n" \
    "⢠⠣⠐⠀    ⭕     ⠀⢪⢺⣪⢣⠀⡀ ⭕   .⠈⡈⠀⡀\n" \
    "⠐⡝⣕⢄⡀⠑⢙⠉⠁⡠⡣⢯⡪⣇⢇⢀⠀⠡⠁⠁⡠⡢⠡\n" \
    "⠀⢑⢕⢧⣣⢐⡄⣄⡍⡎⡮⣳⢽⡸⡸⡊⣧⣢⠀⣕⠜⡌⠌\n" \
    "⠀⠀⠌⡪⡪⠳⣝⢞⡆⡇⡣⡯⣞⢜⡜⡄⡧⡗⡇⠣⡃⡂\n" \
    "⠀⠀⠀⠨⢊⢜⢜⣝⣪⢪⠌⢩⢪⢃⢱⣱⢹⢪⢪⠊\n" \
    "  ⠀⠀⠐⠡⡑⠜⢎⢗⢕⢘⢜⢜⢜⠜⠕⠡⠡⡈\n" \
    "⠀⠀⠀⠀⠀⠁⡢⢀⠈⠨⣂⡐⢅⢕⢐⠁⠡⠡⢁\n" \
    "⠀⠀⠀⠀⠀⠀⢈⠢⠀⡀⡐⡍⢪⢘⠀⠀⠡⡑⡀\n" \
    "⠀⠀⠀⠀⠀⠀⠀⠨⢂⠀⠌⠘⢜⠘⠀⢌⠰⡈\n" \
    "⠀⠀⠀⠀⠀⠀⠀⠀⢑⢸⢌⢖⢠⢀⠪⡂\n\n" \
    "                    L̶̡̛͙͍̜̬̬̣̝͇̼̤̤̣̥͋̽͒͑̄̿̐̋̇͂̃̀o̴̡̨̗͔̜̟̬̤̭̤̙̥̘͋̅͜ͅo̷̦̠̮̹̼̥͎͇̲̰͙͐͌̎̓̈́͂̌̇͜k̵̡̡̢̠̬̜͈̭̻̘̮̼̱̱͍̐̿̈́̅͊͐͊͐̚̚͘͠͠ ̶͓̪̯̗̒̊̃̿͌̈́̂͗͂͝͠b̴̨͇͍͒̀̈͝ͅẹ̴̬̉̍̄͘͠h̴̟͓̻͔͝į̶̧̧̤̦͓͕̑͝n̸͎̻̬̊̄̆̈́̒̃d̸̡̡͓̼͉͈̮͈͖̤͔̎̂͑̍̔̅͋̀̃́̒̕͜ ̴̼̘͙͉̺̮̭̭͍̰̍͗̓̐͂͂͒͒͠y̴̢͖̺̩̗̖̰͙͕̜͖̹͕͒̄ͅǫ̶̢͕̳͖̣͈̰̖̜̙̬̓͌̂͑̉̅̾͆̀̊͜ṵ̵͕͔͙͖̣̾̄̀̃"


dunk = "**DUNK**"


async def dunker(message):
    i = 3
    while i <= 1:
        await message.channel.send(dunk)
        await asyncio.sleep(2)
        i -= 1


async def jubla(message):
    await dunker(message)
    message = await message.channel.send("**jjjjj**")
    for x in jubla_list:
        await asyncio.sleep(1)
        await message.edit(content=x)
