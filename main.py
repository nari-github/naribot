import discord
import os

token = os.getenv("DISCORD_TOKEN") #Your TOKEN

# クライアントの生成
client = discord.Client(intents=discord.Intents.default())

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
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@bot.commands
async def neko(ctx):
    await ctx.send('にゃーん(=^・^=)')

# クライアントの実行
client.run(token)

