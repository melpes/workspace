import discord
from discord.ext import commands
import logging

# logging.basicConfig(level=logging.INFO)

# 외부 파일
import load_json_variable as variable
from load_magic_data import process_data, search_data

prefix = "/"
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    """
    봇이 로딩되었거나 재로딩 되는 경우 실행되는 이벤트

    :return: None
    """

    # 'comment'라는 게임 중으로 설정합니다.
    game = discord.Game("comment")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print("READY")

@bot.event
async def on_message(message):
    # 봇이 메시지를 보낸 경우 어떠한 작업도 하지 않음.
    if message.author.bot:
        return None

    # Commands 이벤트 진행
    await bot.process_commands(message)

@bot.command(name="test")
async def react_test(ctx):
    # 유저가 요청했던 채널로 전송합니다.
    await ctx.channel.send("testing!")
    return None


key = None
data_set = None
skill_name = []

@bot.command(name="매서")
async def react_test(ctx):
    global key, data_set, skill_name
    # 유저가 요청했던 채널로 전송합니다.
    await ctx.channel.send("매직 서바이벌 모드로 전환합니다")
    key = "magic survival"
    data_set = process_data()
    skill_name = [dict["name"] for dict in data_set]
    print(skill_name)
    # 'mode:magic survival'라는 게임 중으로 설정합니다.
    game = discord.Game(f"MODE:{key}")
    await bot.change_presence(status=discord.Status.online, activity=game)
    return None

@bot.command(name="마법")
async def skill(ctx, *names):
    name = ""
    for value in names:
        name += value + " "
    name = name.strip()
    print(name)


    if key != "magic survival":
        await ctx.channel.send("올바른 모드가 아닙니다.")
        return None


    data = search_data(name, data_set)
    msg = ''
    for index, value in data.items():
        msg += f"""{index} : {value}\n"""
    msg = msg.strip()
    await ctx.channel.send(msg)
    return None


@bot.command(name="기본")
async def react_test(ctx):
    global key
    # 유저가 요청했던 채널로 전송합니다.
    await ctx.channel.send("기본 모드로 전환합니다")
    key = "basic"
    # 'mode:basic'라는 게임 중으로 설정합니다.
    game = discord.Game(f"MODE:{key}")
    await bot.change_presence(status=discord.Status.online, activity=game)
    return None

bot.run(variable.get_token())