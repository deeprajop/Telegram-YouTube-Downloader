
from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["info"]), group=-2)
async def love(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("info:", url="https://t.me/Zer0ByteOfficial")],
    ])
    Aww = f"""Hey <b>{message.from_user.first_name}</b>
If you liked my project and want to be a GitHub contributor then:
- 📧You may let us know **@Zer0ByteSupport**
- 🌟You can personal message me in Telegram **@deeprajk**   
- ✨Give Us FeedBack On @Zer0ByteSupport Or Let Us Know Some Bugs If You Encounter\n

If you liked my project and want and just want to make me happy then you can:
- **Share My Bot With Your Friends**
    
**<b>{message.from_user.first_name}</b> Thanks A Lot For Using Zer0Byte**

[Zer0Byte ✘ YT](https://telegra.ph/file/286c0dc385b91a88afda5.jpg)
"""      
    await message.reply_text(Aww, reply_markup=joinButton)
    raise StopPropagation
