import discord
import os
import time
import socket
import sys

allow_ip = os.getenv("ALLOW_IP")

host = socket.gethostname()
ip = socket.gethostbyname(host)

if allow_ip != ip:
    sys.stdout.write("NG:{}".format(ip))
    sys.exit()

sys.stdout.write("OK:{}".format(ip))

token = os.getenv("DISCORD_TOKEN") #Your TOKEN

# インテントの生成
intents = discord.Intents.default()
intents.message_content = True

# クライアントの生成
client = discord.Client(intents=intents)

# discordと接続した時に呼ばれる
@client.event
async def on_ready():
    print('ログインしました')

# メッセージを受信した時に呼ばれる
@client.event
async def on_message(message):
    if message.author.bot:
        message.add_reaction("<:watashi_okage:989196108486033449>")
        return
        
    # 自分のメッセージを無効
    #if message.author == client.user:
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

