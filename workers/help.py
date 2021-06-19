

from pyrogram import Client, Filters

@Client.on_message(Filters.command(["help"]))
async def help(client, message):
    
    # Thought of somemore features but i am lazy lul
    
    helptxt = f"""/help:[📥](https://telegra.ph/file/cd81a45f2a50798d66136.jpg)\n
                 .˜”*°•**InChat**•°*”˜.
Copy any Valid Youtube link and paste inside the bot and follow the prompts.
                 .˜”*°•**InGroups**•°*”˜.
Add me in any group then copy any valid Youtube link and paste inside the bot and follow the prompts.

                .📍**𝐈𝐌𝐏𝐎𝐑𝐓𝐀𝐍𝐓**📍.
-**‼️ Bigger download size,more wait time ‼️**
- File Size More Than 2gbs Cant Be Download Because Of Telegram Policy!!."""
        
    
    await message.reply_text(helptxt)
