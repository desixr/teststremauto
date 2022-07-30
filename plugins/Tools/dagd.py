import requests
from pyrogram import Client, filters

@Client.on_message(filters.command("dagd"))
async def dagd(bot, message):
  
  dagd = await message.reply("`Processing...`")
  
  if len(message.command) == 1:
    return await dagd.edit("No URL provided to short, Read Help Menu to know how command works")
  
  elif len(message.cmmand) == 2:
    url = message.command[1]
    response = requests.get(f"https://da.gd/s?url={url}").text
    await dagd.edit(f"{response}")
  else:
    await dagd.edit("Parameter limit exceeded, Read Help Menu to know how command works.")  
