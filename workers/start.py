

from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔔 Updates:", url="https://t.me/Zer0ByteOfficial")],
        [InlineKeyboardButton("👥 Support:", url="https://t.me/Zer0ByteSupport")],
        [InlineKeyboardButton("✨ Off-Topic", url="https://t.me/Friends_Chatting_Grp")],
        [InlineKeyboardButton("🗃 Source Code", url="https://telegra.ph/file/6d661cc458396796f4692.jpg")],
    ])
    welcomed = f"""
    Hey,
         <b>{message.from_user.first_name}</b>
    Use the below button or type /help for More info.
    [🌟](https://telegra.ph/file/cd81a45f2a50798d66136.jpg)"""
  
    
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
