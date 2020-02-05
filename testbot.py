import discord
import requests
from bs4 import BeautifulSoup
import random
client = discord.Client()

# 생성된 토큰을 입력해준다.
token = "NjQxOTY1NDQyMDUwODE4MDYy.XcQDCA.OjLtz4c7ltzfLmGefIcoalKmwrI"

# 봇이 구동되었을 때 보여지는 코드
@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")
    global RANK , header,req,html,parser,titles,songs,title,song,k,url,learn
    RANK = 10
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
    req = requests.get('https://www.melon.com/chart/index.htm', headers = header)
    html = req.text
    parse = BeautifulSoup(html, 'html.parser')
    titles = parse.find_all("div", {"class": "ellipsis rank01"})
    songs = parse.find_all("div", {"class": "ellipsis rank02"})
    
    title = []
    song = []
    
    learn = []
    url = []
    for t in titles:
            title.append(t.find('a').text)
            url.append(t)
    for s in songs:
            song.append(s.find('span', {"class": "checkEllipsis"}).text)
    
    
# 봇이 특정 메세지를 받고 인식하는 코드
@client.event
async def on_message(message):
    # 메세지를 보낸 사람이 봇일 경우 무시한다
    if message.author.bot:
        return None

    if message.content.startswith('!차트'):
        channel = message.channel
        learn = message.content.split(" ")
        try:
            global RANK
            
            if(int(learn[1]) <= 50 or int(learn[1])>=1):
                RANK = int(learn[1])
            elif learn[1]>=50:
                await channel.send("1~100사이의 수를 입력하세요")
            else:
                await channel.send("1~100사이의 수를 입력하세요")
        except:
            print(learn[0])
        
        global k
        k = ""
        for i in range(RANK):
            k += '%d위: %s - %s'%(i+1, title[i], song[i]+"\n")
            RANK=10
        try:
            await channel.send("```"+k+"```")
        except:
            k="error"
            await channel.send("```"+k+"```")
        
    elif message.content.startswith('!랜덤'):
        channel = message.channel

        
        i = random.randrange(1,101)
        
        k = '%d위: %s - %s'%(i+1, title[i], song[i]+"\n")
        await channel.send("```"+k+"```")
        
        a = str(url[i]).split(",")[1]
        b = a.split(")")[0]
        await channel.send("https://www.melon.com/webplayer/mini.htm?contsIds="+b+"&contsType=S")
        
    

        
client.run(token)










