#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='https://t.me/ANKIT3690'>∞۝Aⲛⲕⲓⲧ۝∞</a>\n\n○ Language : <code>🇮🇳Hindi🇮🇳</code>\n\n○ Active Channel: <a href='https://t.me/defenderofthemultiverse'>𝐃𝐄𝐅𝐄𝐍𝐃𝐄𝐑 𝐎𝐅 𝐓𝐇𝐄 𝐌𝐔𝐋𝐓𝐈𝐕𝐄𝐑𝐒𝐄</a>\n\n○ Main Channel : <a href='https://t.me/+qSjnsXLUV3k0ODg1'>ƬӇҼ ƇRҼⱭƬƠR ƠƑ ƲƝӀVҼRՏҼ</a>\n\n○ Request Group : <a href='https://t.me/thewarriorsreal'>𝓽ꫝꫀ ᥴ𝘳ꫀꪖ𝓽ꪮ𝘳 ꪮᠻ ꪖꪶꪶ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
