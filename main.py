import discord
import os
import sys
import datetime
import calendar

token = os.getenv('DISCORD_TOKEN')  #Your TOKEN

# インテントの生成
intents = discord.Intents.default()
intents.message_content = True

# クライアントの生成
client = discord.Client(intents = intents)

# discordと接続した時に呼ばれる
@client.event
async def on_ready():
  print('login OK')

# メッセージを受信した時に呼ばれる
@client.event
async def on_message(message):
  # 自分のメッセージを無効
  if message.author.bot:
    # https://emojipedia.org/
    await message.add_reaction('⭕')
    await message.add_reaction('🔺')
    await message.add_reaction('❌')
    return

  # メッセージにリアクション追加
  # await message.add_reaction("<:watashi_okage:989196108486033449>")

  # メッセージに反応
  if message.content.startswith('/match'):
    # 設定値
    week_list = ['月', '火', '水', '木', '金', '土', '日', ]
    match_week_list = [2, 5, 6] # レギマ曜日（水、土、日）
    day = 1 # 通知開始日
    league_flg = False
    prefix = ''
    has_league_day = False

    # 引数取得
    args = message.content.split('/match ', 1)
    if args[1:2]:
      month = args[1].split(' ')[0]
      if args[1].split(' ')[1:2]:
        start = args[1].split(' ')[1].split('-')[0]
        end = args[1].split(' ')[1].split('-')[1]
        has_league_day = True
    else:
      month = datetime.datetime.now().month

    date_obj = datetime.datetime.now()
    date_obj = date_obj.replace(month = int(month))
    day_count = calendar.monthrange(date_obj.year, date_obj.month)[1]

    for i in range(day_count):
      date_obj = date_obj.replace(day = day)

      # リーグ期間判定
      if has_league_day:
        if int(start) == day:
          prefix = '＝＝＝＝＝ここからレギリ＝＝＝＝＝\n'
          league_flg = True
  
        if int(end) < day:
          if league_flg == True:
            prefix = '＝＝＝＝＝ここまでレギリ＝＝＝＝＝\n'
            league_flg = False
  
      # リーグ期間中は毎日通知
      if league_flg == True:
        await message.channel.send(prefix + date_obj.strftime('%m/%d') + '（' + week_list[date_obj.weekday()] + '）')
        prefix = ''
      # 特定曜日のみ通知
      elif date_obj.weekday() in match_week_list:
        await message.channel.send(prefix + date_obj.strftime('%m/%d') + '（' + week_list[date_obj.weekday()] + '）')
        prefix = ''
      
      day = day + 1
    return

  if message.content.startswith('/チャーミィ'):
    await message.channel.send('呼んだ？')

# クライアントの実行
client.run(token)
