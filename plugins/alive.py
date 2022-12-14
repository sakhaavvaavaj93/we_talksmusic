import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/309f7a7c61d99977a6fd7.jpg",
        caption=f"""**
ใIt's a Music bot without lag and struck .
  It's a official Music bot of [๐ฃยซยฐฦฦ ฦฎษศดฮส ษ ิผึะขยฐยปโ 2.0](https://t.me/Malayalam_Friends_Chat) 
Nb : Bot and Userbot are locked by owner ,     
**""",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฑ๐๐ก๐๐ค๐๐ฑ", url=f"https://t.me/Malayalam_Friends_Chat"),
                    InlineKeyboardButton(
                        "๐ฑ๐ข๐๐ป๐ฒ๐ฟ๐ฑ", url=f"https://t.me/Lankeshanraavann"),
                    InlineKeyboardButton(
                        "๐ถ๐๐๐๐ถ๐๐๐ฎ๐ป๐๐ถ", url=f"https://t.me/Kanthari_Paru"),
                ]
            ]
        ),
     )
    
    
@Client.on_message(commandpro(["/start", "/alive", "blackcat"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/9dee892784a833fc1344e.jpg",
        caption=f"""**Me on Ultra Fast,Laggless, and No struck** \n๐ฅCommands๐ฅ \n\n`/play` \n\n\`/pause` \n\n`/resume` \n\n`/skip` \n\n`/restart` \n\nadmins only - `pause,resume,restart,skip`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฑเดฐเดพเดตเดฃเตป๐ฑ", url=f"https://t.me/Lankeshanraavann"),
                    InlineKeyboardButton(
                        "๐ถ๐๐๐๐ถ๐๐๐๐ฎ๐ป๐๐ถ", url=f"https://t.me/Kanthari_Paru"),
                ]
            ]
        ),
    )

