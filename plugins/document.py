from pyrogram import Client, filters
from telegraph import Telegraph

telegraph = Telegraph()
telegraph.create_account(short_name="Hagadmansa")

@Client.on_message(filters.command("abcd"))
async def kdneidhd(bot, message):
  
  replied = message.reply_to_message
  
  if replied.document:
    path = (f"./DOWNLOADS/{message.chat.id}.txt")
    await bot.download_media(message=replied, file_name=path)
    k = open(path)
    p = k.read()
    n = p.replace("\n", "<br>")
    if message.command:
      title = message.command[1:]
      if not title:
        title = "Hagadmansa"
    try:
      response = telegraph.create_page(title='Hagadmansa',content=n, author_name="Hagadmansa", author_url="https://hagadmansa.com")
      await message.reply(f"Here is your link:\n\n{response['url']}", disable_web_page_preview=True)
      k.close()
    except Exception as e:
      await message.reply(f"{e}")
      await message.reply(f"{n}")
    