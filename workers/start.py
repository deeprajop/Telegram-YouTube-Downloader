"""
|---------------------------------------------------_____________$$$
|---------------------------------------------------_____________$$$$
|---------------------------------------------------_____________$$$$
|---------------------------------------------------_____________$$$$$
|---------------------------------------------------_____________$$$$$$
|---------------------------------------------------_____________$$$$$$$
|---------------------------------------------------_____________$$$$$$$$
|---------------------------------------------------_____________$$$$$$$$$
|---------------------------------------------------____________$$$__$$$$$$
|---------------------------------------------------____________$$$___$$$$$$
|---------------------------------------------------____________$$$____$$$$$
|---------------------------------------------------____________$$$_____$$$$$
|---------------------------------------------------____________$$$______$$$$
|---------------------------------------------------____________$$$_______$$$$
|---------------------------------------------------____________$$$_______$$$$
|---------------------------------------------------____________$$$________$$$
|---------------------------------------------------____________$$$________$$$
|---------------------------------------------------____________$$$________$$$
|---------------------------------------------------____________$$$________$$
|---------------------------------------------------____________$$________$$$
|---------------------------------------------------____________$$_______$$$
|---------------------------------------------------____________$$______$$$
|---------------------------------------------------_____$$$$$$$$$_____$$$
|---------------------------------------------------___$$$$$$$$$$$___$$$
|---------------------------------------------------_$$$$$$$$$$$$$__$$$
|---------------------------------------------------$$$$$$$$$$$$$$$$$
|---------------------------------------------------$$$$$$$$$$$$$
|---------------------------------------------------$$$$$$$$$$$$
|---------------------------------------------------_$$$$$$$$$
|---------------------------------------------------___$$$$

ʍǟֆȶɛʀʍɨռɖ-ʋʀȶӼ
"""

from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🏠**ᎷᎩ_ᏂᎧᎷᏋ**:", url="https://t.me/musicvrtx")],
        [InlineKeyboardButton("**ʍǟֆȶɛʀʍɨռɖ**", url="https://t.me/phantomxhawk")]
    ])
    welcomed = f"""
    🎈Dear,
        Sir,Ma'am  <b>{message.from_user.first_name}</b>
    Use the below button or type /help for More info.
    [📥](https://telegra.ph/file/62e3a57990afe2d6da431.jpg)
    """
    
    
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
