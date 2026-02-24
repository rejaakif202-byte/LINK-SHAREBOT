from ast import pattern
import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

TG_BOT_TOKEN = "8071086810:AAFmssrJUUCazbNwB5eaGgYwuT9Wudubxt4"
BOT_USERNAME = 'Sukuna_Xprobot'
APP_ID = "32562995"
API_HASH = "d74b9929a577c9e26f72a36397af47d6"
OWNER_ID = "7846306818"
PORT = os.environ.get("PORT", "8080")
DB_URL = "mongodb+srv://interpeterr:interpeterr@cluster0.bh4seqc.mongodb.net/?appName=Cluster0"
DB_NAME = "Cluster0"
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "40"))
COMMAND_PHOTO = "https://graph.org/file/04176cce417d309449f6a-5f60f0333d323168cd.jpg" # Replace with your photo URL
START_PIC = "https://graph.org/file/04176cce417d309449f6a-5f60f0333d323168cd.jpg"
START_MSG = "ʜᴇʟʟᴏ ᴛʜᴇʀᴇ! {mention} ~\n\n <i><b><blockquote>I ᴀᴍ ᴀ ᴀᴅᴠᴀɴᴄᴇ ʟɪɴᴋ sʜᴀʀᴇ ʙᴏᴛ ᴛʜʀᴏᴜɢʜ ᴡʜɪᴄʜ ʏᴏᴜ ᴄᴀɴ ɢᴇᴛ ᴛʜᴇ ʟɪɴᴋs ᴏғ sᴘᴇᴄɪғɪᴄ ᴄʜᴀɴɴᴇʟs ᴡʜɪᴄʜ sᴀᴠᴇ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟs ғʀᴏᴍ ᴄᴏᴘʏʀɪɡʜᴛ.</blockquote></b></i>"
ABOUT_TXT = "<i><b><blockquote>◈ ᴄʀᴇᴀᴛᴏʀ: <a href='tg://openmessage?user_id=7846306818'>sʜᴀᴍʀᴏᴄᴋ</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href='https://t.me/animexverse'>ᴀɴɪᴍᴇ ᴠᴇʀsᴇ</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href='tg://openmessage?user_id=7846306818'>sʜᴀᴍʀᴏᴄᴋ</a>\n◈ ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>ᴍᴏɴɢᴏ ᴅʙ</a>\n» ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href='tg://openmessage?user_id=7846306818'>sʜᴀᴍʀᴏᴄᴋ</a></blockquote></b></i>"
HELP_TXT = "⁉️ ʜᴇʟʟᴏ ᴛʜᴇʀᴇ! {mention} ~\n\n <b><blockquote expandable>➪ I ᴀᴍ ᴀ ᴘʀɪᴠᴀᴛᴇ ʟɪɴᴋ sʜᴀʀɪɴɢ ʙᴏᴛ, ᴍᴇᴀɴᴛ ᴛᴏ ᴘʀᴏᴠɪᴅᴇ ʟɪɴᴋ ғᴏʀ sᴘᴇᴄɪғɪᴄ ᴄʜᴀɴɴᴇʟs.\n\n ➪ Iɴ ᴏʀᴅᴇʀ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʟɪɴᴋs ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ ᴀʟʟ ᴍᴇɴᴛɪᴏɴᴇᴅ ᴄʜᴀɴɴᴇʟ ᴛʜᴀᴛ ɪ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴛᴏ ᴊᴏɪɴ. Yᴏᴜ ᴄᴀɴ ɴᴏᴛ ᴀᴄᴄᴇss ᴏʀ ɢᴇᴛ ᴛʜᴇ ғɪʟᴇs ᴜɴʟᴇss ʏᴏᴜ ᴊᴏɪɴᴇᴅ ᴀʟʟ ᴄʜᴀɴɴᴇʟs.\n\n ‣ /help - Oᴘᴇɴ ᴛʜɪs ʜᴇʟᴘ ᴍᴇssᴀɢᴇ !</blockquote></b>"
FSUB_PIC = "https://graph.org/file/04176cce417d309449f6a-5f60f0333d323168cd.jpg"
FSUB_LINK_EXPIRY = 300
LOG_FILE_NAME = "SukunaLogChannel.txt"
DATABASE_CHANNEL = "-1003863273872"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
