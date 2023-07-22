import discord
import os
import time
import socket
import sys
import requests

allow_ip = os.getenv("ALLOW_IP")

#host = socket.gethostname()
#ip = socket.gethostbyname(host)
my_ip = requests.get('https://ifconfig.me')

if allow_ip != my_ip.text:
    sys.stdout.write("NG:{}".format(my_ip.text))
    sys.exit()

sys.stdout.write("OK:{}".format(my_ip.text))

token = os.getenv("DISCORD_TOKEN") #Your TOKEN

# インテントの生成
intents = discord.Intents.default()
intents.message_content = True

# クライアントの生成
client = discord.Client(intents=intents)

# discordと接続した時に呼ばれる
@client.event
async def on_ready():
    sys.stdout.write("ログインしました")

# メッセージを受信した時に呼ばれる
@client.event
async def on_message(message):
    if message.author.bot:
        sys.stdout.write("1つ目")
        message.add_reaction("<:watashi_okage:989196108486033449>")
        return
        
    # 自分のメッセージを無効
    if message.author == client.user:
        sys.stdout.write("2つ目")
        message.add_reaction("<:watashi_okage:989196108486033449>")
        return
    #    time.sleep(1)
    #    await message.add_reaction(":o:")
    #    time.sleep(1)
    #    await message.add_reaction(":small_red_triangle:")
    #    time.sleep(1)
    #    await message.add_reaction(":x:")
    #    return

    # メッセージにリアクション追加
    # emoji ="👍"
    #await message.add_reaction("<:watashi_okage:989196108486033449>")

    # メッセージが"$hello"で始まっていたら"Hello!"と応答
    if message.content.startswith('$neko'):
        await message.channel.send('にゃーん(=^・^=)')
        return

    if message.content.startswith('/レギマ'):
        time.sleep(1)
        await message.channel.send('7/20（日）')
        return

# クライアントの実行
client.run(token)
