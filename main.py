import discord
from discord.ext import commands
import getMeal
import os
from keep_alive import keep_alive
from datetime import datetime
from pytz import timezone

app = commands.Bot(command_prefix='!')


@app.event
async def on_ready():
	print('다음으로 로그인합니다: ')
	print(app.user.name)
	# 상태 메시지 설정
	# 종류는 3가지: Game, Streaming, CustomActivity
	game = discord.Game("!도움 for help ")
	await app.change_presence(
	    status=discord.Status.online, activity=game)  # 온라인 상태, game 중으로 설정

	print('connection was succesful')


@app.command(description='For when you wanna know today\'s lunch menu')
async def 중식(ctx):
	c = str(getMeal.getLunch())
	embed = discord.Embed(
	    title="**Whats Meal**", description='', color=15105570)
	embed.add_field(name=getMeal.dateInfo() + "의 점심메뉴", value=c, inline=False)
	await ctx.send(embed=embed)


@app.command(description='For when you wanna know how to use this bot')
async def 도움(ctx):
	embed = discord.Embed(
	    title="**KS Meal Notification**",
	    description="경상고 급식 알리미 봇 입니다 (*´∪`)\n",
	    color=0x62c1cc)
	embed.add_field(name="**!중식**", value="`오늘의 점심메뉴를 안내합니다.`", inline=True)
	embed.add_field(name="**!석식**", value="`오늘의 저녁메뉴를 안내합니다.`", inline=True)
	embed.add_field(
	    name="**!메뉴 <mm> <dd>**",
	    value="`지정한 날짜의 급식을 안내합니다.<중식만 제공 중>`",
	    inline=False)
	embed.add_field(name="**!예시**", value="`명령어 사용 예시를 보여줍니다`", inline=False)
	embed.set_footer(
	    text="아키티오#9732 [도움 : khw#2662]",
	    icon_url="https://i.imgur.com/gqhyveT.png")
	await ctx.send(embed=embed)


@app.command(description='For when you wanna know today\'s dinner menu')
async def 석식(ctx):
	c = str(getMeal.getDinner())
	if c == "None":
		c = "오늘은 석식이 없네요 ＼(´◓Д◔`)／"
	embed = discord.Embed(
	    title="**Whats Meal**", description='', color=15105570)
	embed.add_field(
	    name=getMeal.dateInfo() + "의 저녁메뉴",
	    value="```" + c + "```",
	    inline=False)
	await ctx.send(embed=embed)


@app.command(
    description='For when you wanna know meal menu with specific date')
async def 메뉴(ctx, *args):
	if not args:
		await ctx.send("날짜를 입력하세요")
	else:
		c = "**중식**\n" + str(getMeal.getLunch(args[0], args[1]))
		embed = discord.Embed(
		    title="**Whats Meal**", description='', color=15105570)
		embed.add_field(
		    name=args[0] + "/" + args[1] + "의 메뉴(중식)", value=c, inline=False)
		await ctx.send(embed=embed)


@app.command(description='For when you wanna know how to use commands')
async def 예시(ctx):
	embed = discord.Embed(
	    title="**Whats Commands**", description='', color=2067276)
	embed.add_field(name="**중식**", value="!중식", inline=True)
	embed.add_field(name="**석식**", value="!석식", inline=True)
	embed.add_field(name="**메뉴**", value="!메뉴 12 24", inline=False)
	await ctx.send(embed=embed)

@app.command(description='For when you wanna know what server time is')
async def 시간(ctx):
  whatTime = str(datetime.now(timezone('Asia/Seoul')).strftime("%Y%m%d-%H%M%S"))
  await ctx.send("> 현재 서버 시간 : " + whatTime) 

keep_alive()
app.run(os.getenv('TOKEN'))
