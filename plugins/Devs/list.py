import os
import glob
from info import ADMINS
from pyrogram import Client, filters
from plugins.Helper.humanbytes import humanbytes

@Client.on_message(filters.command("list") & filters.user(ADMINS))
async def list(bot, message):
  
  list = await message.reply("`Processing...`")

  files = message.command[1]
  if not files:
      files = "*"
  elif files.endswith("/"):
      files += "*"
  elif "*" not in files:
      files += "/*"
  files = glob.glob(files)
  if not files:
      return await list.edit("Directory Empty or Incorrect.")
  pyfiles = []
  jsons = []
  vdos = []
  audios = []
  pics = []
  others = []
  otherfiles = []
  folders = []
  text = []
  apk = []
  exe = []
  zip_ = []
  book = []
  for file in sorted(files):
      if os.path.isdir(file):
           folders.append("📂 " + str(file))
      elif str(file).endswith(".py"):
          pyfiles.append("🐍 " + str(file))
      elif str(file).endswith(".json"):
          jsons.append("🔮 " + str(file))
      elif str(file).endswith((".mkv", ".mp4", ".avi", ".gif", "webm")):
          vdos.append("🎥 " + str(file))
      elif str(file).endswith((".mp3", ".ogg", ".m4a", ".opus")):
          audios.append("🔊 " + str(file))
      elif str(file).endswith((".jpg", ".jpeg", ".png", ".webp", ".ico")):
          pics.append("🖼 " + str(file))
      elif str(file).endswith((".txt", ".text", ".log")):
          text.append("📄 " + str(file))
      elif str(file).endswith((".apk", ".xapk")):
          apk.append("📲 " + str(file))
      elif str(file).endswith((".exe", ".iso")):
          exe.append("⚙ " + str(file))
      elif str(file).endswith((".zip", ".rar")):
          zip_.append("🗜 " + str(file))
      elif str(file).endswith((".pdf", ".epub")):
          book.append("📗 " + str(file))
      elif "." in str(file)[1:]:
          others.append("🏷 " + str(file))
      else:
          otherfiles.append("📒 " + str(file))
  omk = [
      *sorted(folders),
      *sorted(pyfiles),
      *sorted(jsons),
      *sorted(zip_),
      *sorted(vdos),
      *sorted(pics),
      *sorted(audios),
      *sorted(apk),
      *sorted(exe),
      *sorted(book),
      *sorted(text),
      *sorted(others),
      *sorted(otherfiles),
  ]
  text = ""
  fls, fos = 0, 0
  flc, foc = 0, 0
  for i in omk:
      try:
          emoji = i.split()[0]
          name = i.split(maxsplit=1)[1]
          nam = name.split("/")[-1]
          if os.path.isdir(name):
              size = 0
              for path, dirs, files in os.walk(name):
                  for f in files:
                      fp = os.path.join(path, f)
                      size += os.path.getsize(fp)
              if hb(size):
                  text += emoji + f" `{nam}`" + "  `" + hb(size) + "`\n"
                  fos += size
              else:
                  text += emoji + f" `{nam}`" + "\n"
              foc += 1
          else:
              if hb(int(os.path.getsize(name))):
                  text += (
                      emoji
                      + f" `{nam}`"
                      + "  `"
                      + hb(int(os.path.getsize(name)))
                      + "`\n"
                  )
                  fls += int(os.path.getsize(name))
              else:
                  text += emoji + f" `{nam}`" + "\n"
              flc += 1
      except:
          pass
  tfos, tfls, ttol = hb(fos), hb(fls), hb(fos + fls)
  if not hb(fos):
      tfos = "0 B"
  if not hb(fls):
      tfls = "0 B"
  if not hb(fos + fls):
      ttol = "0 B"
  text += f"\n\n`Folders` :  `{foc}` :   `{tfos}`\n`Files` :       `{flc}` :   `{tfls}`\n`Total` :       `{flc+foc}` :   `{ttol}`"
  try:
      await list.edit(text)
  except:
      with io.BytesIO(str.encode(text)) as out_file:
          out_file.name = "list.txt"
          await message.replydocument(file=out_file, caption=f"`{e.text}`", thumb="resources/devoloper.png")
      await list.delete()
