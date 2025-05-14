from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream.input_stream import AudioPiped
from yt_dlp import YoutubeDL
import asyncio

from main import app
pytgcalls = PyTgCalls(app)

ydl_opts = {
    "format": "bestaudio/best",
    "quiet": True,
    "noplaylist": True,
}

@pytgcalls.on_stream_end()
async def stream_end_handler(_, update: Update):
    await pytgcalls.leave_group_call(update.chat_id)

@app.on_message(filters.command("play") & filters.group)
async def play_handler(client, message):
    if len(message.command) < 2:
        await message.reply("Please provide a song name. Example: /play sanam teri kasam", quote=True)
        return

    query = " ".join(message.command[1:])
    await message.reply(f"Searching and downloading *{query}*...")

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=False)["entries"][0]
        url = info["url"]

    await pytgcalls.join_group_call(
        message.chat.id,
        AudioPiped(url)
    )
    await message.reply(f"Now playing: *{info['title']}*")

async def main():
    await app.start()
    await pytgcalls.start()
    print("Bot is online...")
    await idle()

if _name_ == "_main_":
    asyncio.run(main())