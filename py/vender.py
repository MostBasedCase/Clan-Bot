import requests
import discord
import datetime
import asyncio
from discord.ext import commands
import time
import sched
import random
import colorsys
from termcolor import colored

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
            phrase = "```css\npossibly-dropping-300\n```"
        elif x['type'] == 3:
            phrase = "```css\nlikely-dropping-300\n```"
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


@client.command(pass_context=True)
async def ggez():
    roll = random.randint(0, 14)
    if roll == 0:
        return await client.say("Ah shucks... you guys are the best!")
    elif roll == 1:
        return await client.say("C’mon, Mom! One more game before you tuck me in. Oops mistell.")
    elif roll == 2:
        return await client.say("For glory and honor! Huzzah comrades!")
    elif roll == 3:
        return await client.say("Gee whiz! That was fun. Good playing!")
    elif roll == 4:
        return await client.say("Good game! Best of luck to you all!")
    elif roll == 5:
        return await client.say("Great game, everyone!")
    elif roll == 6:
        return await client.say("I could really use a hug right now.")
    elif roll == 7:
        return await client.say("I feel very, very small... please hold me...")
    elif roll == 8:
        return await client.say("I'm trying to be a nicer person. It's hard, but I am trying guys.")
    elif roll == 9:
        return await client.say("I'm wrestling with some insecurity issues in my life but thank you all for playing with me.")
    elif roll == 10:
        return await client.say("It was an honor to play with you all. Thank you.")
    elif roll == 11:
        return await client.say("It’s past my bedtime. Please don’t tell my mommy.")
    elif roll == 12:
        return await client.say("Mommy says people my age shouldn’t suck their thumbs.")
    elif roll == 13:
        return await client.say("Well played. I salute you all.")
    elif roll == 14:
        return await client.say("Wishing you all the best.")

def get_channel(channels, channel_name):
    for channel in client.get_all_channels():
        if channel.name == channel_name:
            return channel
    return None


@client.command(pass_context=True)
async def commands():
    em = discord.Embed(title="!engrams", description="Gets all level engrams and weapons from vendors (must be base 300 or level 305)",
                       color=discord.Color.green())
    em.add_field(name="!ggez", value="hehe xD", inline=True)
    em.add_field(name="!commands", value="Wait didn't you just type this?!?!", inline=True)
    em.add_field(name="!nani", value="Omae wa mou...", inline=True)
    return await client.say(embed=em)


@client.command(pass_context=True)
async def nani():
    up = get_channel(client.get_all_channels(), 'off-topic')
    roll = random.randint(0, 4)
    if roll == 0:
        await asyncio.sleep(1)
        return await client.send_file(up, "lol.jpg")
    elif roll == 1:
        await asyncio.sleep(1)
        return await client.send_file(up, "dedede.png")
    elif roll == 2:
        await asyncio.sleep(1)
        return await client.send_file(up, "nani.gif")
    elif roll == 3:
        await asyncio.sleep(1)
        return await client.send_file(up, "xd.jpg")
    elif roll == 4:
        await asyncio.sleep(1)
        return await client.send_file(up, "swswsw.jpg")

client.run("Mzc5ODQ1NTQyMjM2Mzg5Mzc2.DOwgGA.nOpDMALFayuOcvfcy5zRJyNBfjc")






