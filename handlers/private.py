from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/5ec14afc83414136362b0.jpg")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🖤
I Cᴀɴ Pʟᴀʏ Mᴜsɪᴄ Iɴ Yᴏᴜʀ Gʀᴏᴜᴩ Vᴏɪᴄᴇ Cʜᴀᴛ. Dᴇᴠᴇʟᴏᴩᴇᴅ Bʏ [🇮🇳 #𝐃𝐄𝐕𝐈𝐋 🇮🇳](https://t.me/ITX_DEVIL_OP).
Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴩ Aɴᴅ Pʟᴀʏ Mᴜsɪᴄ Fʀᴇᴇʟʏ!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Oᴡɴᴇʀ 🇮🇳", url="t.me/ITX_DEVIL_OP")
                  ],[
                    InlineKeyboardButton(
                        "Sᴜᴩᴩᴏʀᴛ 😙", url="https://t.me/KIRA_SUPPORT"
                    ),
                    InlineKeyboardButton(
                        "Cʜᴀɴɴᴇʟ", url="https://t.me/KIRA_UPDATES"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ➕", url="https://t.me/LIGHT_YAGAMI_ROBOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Aᴍ Oɴʟɪɴᴇ ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊Uᴩᴅᴀᴛᴇs", url="https://t.me/KIRA_UPDATES")
                ]
            ]
        )
   )
