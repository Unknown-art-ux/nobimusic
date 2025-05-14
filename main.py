from pyrogram import Client, filters
from pyrogram.types import Message

api_id = 28366400
api_hash = "7b4e2aa384a812ab717f7f525383591c"
bot_token = "8025600005:AAEFWnD6-q7EyJUoKx3A1D1ZKjRUoiOSvGw"

app = Client("music_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@app.on_message(filters.command("start"))
async def start(client, message: Message):
    await message.reply("Hi! I'm your music bot. Use /play <song name> to play music.")


@app.on_message(filters.command("help"))
async def help_command(client, message: Message):
    await message.reply("/play <song> - play music\n/vplay <video> - play video\n/skip, /pause, /resume, /seek - control music")


app.run()