from pyrogram import Client, filters
from plugins.Helper.async_searcher import async_searcher

@Client.on_message(filters.command("meaning"))
async def meaning(bot, message):
  
  meaning = await message.reply("`Processing...`")
  
  if len(message.command) == 1:
     return await meaning.edit("No word provided to find meaning, Read Help Menu to know how command works")
    
  elif len(message.command) == 2:
    word = message.command[1]
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + word
    out = await async_searcher(url, re_json=True)
    try:
        return await meaning.edit(f'{out["title"]} For Word `{word}`.')
    except (KeyError, TypeError):
        pass
    defi = out[0]["meanings"][0]["definitions"][0]
    ex = "None" if not defi.get("example") else defi["example"]
    text = f"**• Word: **`{word}`\n**• Meaning: **`{defi["definition"]}`\n**• Example: **__{ex}__"
    if len(text) > 4096: 
        with io.BytesIO(str.encode(text)) as file: 
            file.name = f"{wrd}-meaning.txt"
            await message.reply_document(document=file, caption=f"Meanings of {word}", thumb="resources/devoloper.png")
            return await meaning.delete()
    else:
        await meaning.edit(text)
  else:
    await meaning.edit("Parameter limit exceeded, Read Help Menu to know how command works.")
