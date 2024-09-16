# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/ca6ca3ca0cae0e2f9b3d9.jpg",
    "https://telegra.ph/file/40e5bff51bdf7d0b51c54.jpg",
    "https://telegra.ph/file/2db177a58e156bb3b697e.jpg",
    "https://graph.org/file/0ce0901a95ec7cd5897df.jpg",
    "https://graph.org/file/88007011ac6e07b92aa92.jpg",
    "https://graph.org/file/9db70cb7ab32299aad914.jpg",
    "https://graph.org/file/77f3c9955282f900213de.jpg",
]

HEY_IMG = "https://graph.org/file/b3410bcd7f85c3b6c448b.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph/file/90eaa26f876190f90155a.mp4",
    "https://telegra.ph/file/66432194b53ff55538556.mp4",
    "https://telegra.ph/file/90eaa26f876190f90155a.mp4",
    "https://telegra.ph/file/66432194b53ff55538556.mp4",
    "https://telegra.ph/file/90eaa26f876190f90155a.mp4",
    "https://telegra.ph/file/66432194b53ff55538556.mp4",
    "https://telegra.ph/file/90eaa26f876190f90155a.mp4",
    "https://telegra.ph/file/66432194b53ff55538556.mp4",
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* `{}` . . ."

PM_START_TEXT = "✨ *ɪ ᴀᴍ 𝙃𝙪 𝙩𝙖𝙤, ᴀ ɢᴇɴꜱʜɪɴ ɪᴍᴘᴀᴄᴛ ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="HELP", callback_data="extra_command_handler"),
    ],
    [
        InlineKeyboardButton(text="DETAILS", callback_data="Miko_"),
        InlineKeyboardButton(text="SOURCE", callback_data="git_source"),
    ],
    [
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/beasts_network"),
        ib(text="SUPPORT", url="https://t.me/beasts_community"),
    ],
    [
        ib(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *𝙃𝙪 𝙩𝙖𝙤* 🫧 [ㅤ](https://telegra.ph/file/b05535884267a19ee5c93.jpg)

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
