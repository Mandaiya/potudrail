

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from InsaneMusic import app
from InsaneMusic.core.call import Insane
from InsaneMusic.utils.database import is_music_playing, music_off
from InsaneMusic.utils.decorators import AdminRightsCheck

# Commands
PAUSE_COMMAND = get_command("PAUSE_COMMAND")


@app.on_message(
    filters.command(PAUSE_COMMAND) & filters.group & ~filters.edited & ~BANNED_USERS
)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])        
    await music_off(chat_id)
    await Insane.pause_stream(chat_id)
    await message.send_video(
        video="https://telegra.ph/file/e755ce78fd425bbcb696f.mp4",
        caption=_["admin_2"].format(message.from_user.mention)        
    )
