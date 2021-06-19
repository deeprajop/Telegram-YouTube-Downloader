
from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["youtubelink"]), group=-2)
async def love(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("⚡️ EDM:", url="https://t.me/Friends_Chatting_Grp")],
        [InlineKeyboardButton("❄️ LO-FI:", url="https://t.me/Friends_Chatting_Grp")],
        [InlineKeyboardButton("✨ TRAP-BEAT:", url="https://t.me/Friends_Chatting_Grp")],
        [InlineKeyboardButton("🔥 𝗡𝗖𝗦:", url="https://t.me/Friends_Chatting_Grp")],
        [InlineKeyboardButton("🌟 𝗣𝗢𝗣:", url="https://t.me/Friends_Chatting_Grp")]
    ])
    youtube_ex = f"""
**Some example youtube channels and songs if you don't know what u want**📺
- type /info if Zer0Byte Helped u anyway!!
"""

   
    
    await message.reply_text(youtube_ex, reply_markup=joinButton)
    raise StopPropagation






