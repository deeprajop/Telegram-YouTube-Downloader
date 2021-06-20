

from pyrogram import Client, Filters

@Client.on_message(Filters.command(["help"]))
async def help(client, message):
    
    # Thought of somemore features but i am lazy lul
    
    helptxt = f"""Zer0Byte ✘ YT:[🗒](https://telegra.ph/file/cd81a45f2a50798d66136.jpg)\n
🔮Commands

❄️ In Bot dm : 
• Send any Valid Youtube link
• Select the quality and format that you want the video to be downloaded in.
• Wait while the bot provides you with the video.

❄️ In groups : 
• Add me in any group then sent any valid youtube link.
• Select the quality and format that you want the video to be downloaded in.
• Wait while the bot provides you with the video.

⚠️ NOTE
-‼️ Bigger Download Size, More Wait Time.
- File Size More Than 2GB Cant Be Download Because Of Telegram Restrictions!! 
"""
        
    
    await message.reply_text(helptxt)
