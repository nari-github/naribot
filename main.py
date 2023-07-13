import discord
import os

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
    # 自分のメッセージを無効
    if message.author == client.user:
        return

    # メッセージにリアクション追加
    emoji ="👍"
    await message.add_reaction(emoji)

    # メッセージが"$hello"で始まっていたら"Hello!"と応答
    if message.content.startswith('$neko'):
        await message.channel.send('にゃーん(=^・^=)')

# クライアントの実行
client.run(token)

