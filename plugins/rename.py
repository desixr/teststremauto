import os
import time
from info import ADMINS
from pyrogram import Client, filters 
from plugins.Helper.progress import progress
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

def listToString(s):
  str1 = " "
  return (str1.join(s))
  
@Client.on_message(filters.command('rename') & filters.user(ADMINS))
async def rename(bot, message):
  
    rn = await message.reply("`Trying to download...`")
    replied = message.reply_to_message
    
    if (" " in message.text) and (message.reply_to_message is not None):
      
        filename = message.command[1:]
        file_name = listToString(filename)
        
        if len(file_name) > 128:
            return await rn.edit('File name can not be longer than 128 alphabets.')
        
        time_ = time.time()
        the_real_download_location = await bot.download_media(
            message=replied,
            progress=progress,
            progress_args=('Downloading...', rn, time_)
        )
 
        os.rename(the_real_download_location, file_name)
        await rn.edit("`Trying to upload...`")  
            
        time_ = time.time()
        await message.reply_document(
            document=file_name,
            thumb='resources/devoloper.png',
            caption=file_name,
            progress=progress,
            progress_args=('Uploading...', rn, time_)
        )
        os.remove(file_name)
        await rn.edit('Successfully Uploaded.')
    else:
        await rn.edit('Reply to file and provide a new name')
    