import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "23049826"))
  API_HASH = os.environ.get("API_HASH", "4a4216f089ce68a3ce2c8b9b9a6fa79a")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "Toons1_Robot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002096181518"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "hidden2history.in")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "d1bda24c40588198951f1c18426c69ceefcb0fb5")
  START_PIC = os.environ.get("START_PIC","https://telegra.ph/file/8b710c2ff0d3fa50c4228.jpg")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "2135601715"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://aman:hdhub4net@cluster0.f6fbxm4.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002097023238"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 


╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [Gi Cartoons Network✨](https://telegram.me/addlist/CCrTT1vAeBRiMDQ1)
 
Just Send Me Video Or File I Will Give You Permanent Sharaable Link.
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

Made By @Gi_Tamil_Cartoons
"""
