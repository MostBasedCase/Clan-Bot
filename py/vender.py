import requests
import discord
import datetime
import asyncio
from discord.ext import commands
import time
import sched

client = discord.Client()
prefix = "!"
client = commands.Bot(command_prefix=prefix)


@client.command(pass_context=True)
async def engrams():
    a = requests.get("https://api.vendorengrams.xyz/getVendorDrops?key=e4f84ef719066f926b97d4290dbae721&vendor=0")

    aj = a.json()
    vendor = [("Arach Jalaal", 15, str("")), ("Asher Mir", 4, str("")), ("Banshee-44", 10, str("")),
              ("Benedict 99-40", 12, str("")), ("Commander Zavala", 8, str(""))
        , ("Devrim Kay", 0, str("")), ("Drang", 7, str("")), ("Executor Hideo", 14, str("")), ("Failsafe", 3, str("")),
              ("Ikora Rey", 11, str(""))
        , ("Lakshmi-2", 13, str("")), ("Lord Saladin", 17, str("")), ("Lord Shaxx", 9, str("")),
              ("Man 'O War", 5, str("")), ("MIDA Mini-Tool", 1, str(""))
        , ("Sloane", 2, str("")), ("The Emissary", 16, str(""))]

    for x in aj:
        if x['type'] == 0:
            phrase = "dropping 295"
        elif x['type'] == 1:
            phrase = "dropping 296-299"
        elif x['type'] == 2:
            phrase = "possibly dropping 300"
        elif x['type'] == 3:
            phrase = "likely dropping 300"
        else:
            phrase = "need more data."
        count = -1
        for p in vendor:
            count += 1
            if x['vendor'] == p[1]:
                p = (p[0], p[1], phrase)
                vendor[count] = p
    minute = datetime.datetime.now().minute
    sec = datetime.datetime.now().second
    min_remain = 30 - datetime.datetime.now().minute
    sec_remain = 60 - datetime.datetime.now().second
    if min_remain < 0:
        min_remain = 60 - datetime.datetime.now().minute

    if sec < 10:
        sec = str(0) + str(sec)
    if minute < 10:
        minute = str(0) + str(minute)

    tex = str(datetime.datetime.now().hour) + \
        ":" + str(minute) \
        + ":" + str(sec) + " EST | " \
        "Reset in : " + "\n" + str(
        min_remain) + " minute(s) and " + str(sec_remain) + " second(s)"

    em = discord.Embed(title="", description="", color=discord.Color.blue())
    for z in vendor:
        em.add_field(name=z[0], value=z[2], inline=True)
    em.set_footer(text=tex)
    return await client.say(embed=em)



client.run("{Bot Token}")






