import discord, asyncio, datetime, random
import os
#from discord.colour import Color
#from discord.enums import PremiumType


token = " "
client = discord.Client()

@client.event
async def on_ready():
    print("봇 준비 완료!")
    print(client.user)
    print("=================================")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("!도움"))

@client.event
async def on_message(message):
    if message.content == "ping":
        await message.channel.send("pong")

    if message.content == "!도움":
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.blue(), title="수성봇 명령어")
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        embed.add_field(name="!도움", value="명령어 목록", inline=False)
        embed.add_field(name="!채널", value="!채널 <채널 아이디> <할말> [관리자 전용]", inline=False)
        embed.add_field(name="!정보", value="디스코드 개인 프로필 정보", inline=False)
        embed.add_field(name="!랜덤번호", value="1~26까지의 숫자가 랜덤으로 나옴", inline=False)
        embed.add_field(name="!타이머", value="60초 타이머", inline=False)
        embed.add_field(name="!시간표", value="수성고 1학년 11반 시간표", inline=False)
        embed.add_field(name="!11반", value="수성고 1학년 11반 학번이름", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith(f"!채널"):
        if message.author.guild_permissions.administrator:
            ch = client.get_channel(int(message.content[4:22]))
            await ch.send(message.content[23:])

    if message.content.startswith("!정보"):
            date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >>22) + 1420070400000) / 1000)
            embed = colour=discord.Colour.blue()
            embed.add_field(name="이름", value=message.author.name, inline=False)
            embed.add_field(name="서버닉네임", value=message.author.display_name, inline=False)
            embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" +  str(date.day) + "일", inline=False)
            embed.add_field(name="아이디", value=message.author.id, inline=False)
            embed.set_thumbnail(url=message.author.avatar_url)
            
            await message.channel.send(embed=embed)

    msg = message.content

    if message.content == "!랜덤번호":
        await message.channel.send(random.randint(1,26))

    if message.content == "!타이머":
        await message.channel.send(f"{message.author.mention}, 60초 뒤 태그해서 알려드릴께요!")
        await asyncio.sleep(60)
        await message.channel.send(f"{message.author.mention}, 시간이 지났어요!")

    if message.content == "!시간표":
        await message.channel.send("https://cdn.discordapp.com/attachments/840850434583298103/954741893655310386/BandPhoto_2022_02_25_21_07_23.jpg")
        await message.channel.send("https://cdn.discordapp.com/attachments/840850434583298103/955387740189503538/20220321_170441.jpg")

    if message.content == "!11반":
        await message.channel.send("담임: 김인영\n11101 박준우 11102 김동환 11103 김민혁 11104 김선욱 11105 김영범\n11106 김이안 11107 김한울 11108 이준봉 11109 박선우 11110 박신영\n11111 박재헌 11112 박정우 11113 손찬영 11114 송정헌 박선우 11115 이승준\n11116 이주호 11117 임재선 11118 임진성 11119 정진섭 11120 채종엽\n11121 최경서 11122 최진재 11123 황인성 11124 황지효 11125 김세현\n11126 김지수")






























































































access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
