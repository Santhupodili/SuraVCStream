# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from program.utils.inline import menu_markup
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"""👋 **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
🤖 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ🎶 ᴀɴᴅ ᴠɪᴅᴇᴏ🎥 ᴏɴ ɢʀᴏᴜᴘs ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ!**

💚 **ғɪɴᴅ ᴏᴜᴛ ᴀʟʟ ᴛʜᴇ ʙᴏᴛ's ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ʜᴏᴡ ᴛʜᴇʏ ᴡᴏʀᴋ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ » 🛠️ ᴄʜᴇᴄᴋ ᴄᴏᴍᴍᴀɴᴅs ʙᴜᴛᴛᴏɴ!**

💝 **ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ, ᴘʟᴇᴀsᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ » 💚 ʀᴇᴀᴅ ʙᴀsɪᴄ ɢᴜɪᴅᴇ ʙᴜᴛᴛᴏɴ **
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💙 ɴᴀɴᴜ ᴀᴅᴅ ᴄʜᴇsᴜ ᴋᴏʀᴀ ɴɪʙʙᴀ 💞",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("💗 ʙᴀsɪᴄ ɢᴜɪᴅᴇ ʀᴀ ɴɪʙʙᴀ 🤍", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("✅ sᴀɴᴛʜᴜ ᴄᴏᴍᴍᴀɴs 💘", callback_data="cbcmds"),
                    InlineKeyboardButton("🔰 ᴅᴏɴᴀᴛᴇ ʀᴀ ɴɪʙʙᴀ 🔰", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "💖 ɢʀᴏᴜᴘ ʀᴀ ɴɪʙʙᴀ 💞", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "💝 sᴀɴᴛʜᴜ ɴᴇᴛᴡᴏʀᴋ 🤎", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "❤ ʏᴏᴜᴛᴜʙᴇ 💚", url="https://youtube.com/channel/UC7QMr8IDR65vciXrwx4XLiQ"
                    )
                ],
                [    InlineKeyboardButton(
                    "💛 ᴄᴏᴍᴍᴀɴᴅs 💔", url="https://telegra.ph/TITLE-02-09-53"
                     )
                ], 
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f"""🤔 ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ?, ʀᴇᴀᴅ ᴛʜᴇ ɢᴜɪᴅᴇ ʙᴇʟᴏᴡ !

𝟷.) ғɪʀsᴛ, ᴀᴅᴅ ᴛʜɪs ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
𝟸.) ᴛʜᴇɴ, ᴘʀᴏᴍᴏᴛᴇ ᴛʜɪs ʙᴏᴛ ᴀs ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀ ᴏɴ ᴛʜᴇ ɢʀᴏᴜᴘ ᴀʟsᴏ ɢɪᴠᴇ ᴀʟʟ ᴘᴇʀᴍɪssɪᴏɴs ᴇxᴄᴇᴘᴛ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ.
𝟹.) ᴀғᴛᴇʀ ᴘʀᴏᴍᴏᴛɪɴɢ ᴛʜɪs ʙᴏᴛ, ᴛʏᴘᴇ /reload ɪɴ ɢʀᴏᴜᴘ ᴛᴏ ᴜᴘᴅᴀᴛᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴅᴀᴛᴀ.
𝟹.) ɪɴᴠɪᴛᴇ @{ASSISTANT_NAME} ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴏʀ ᴛʏᴘᴇ /userbotjoin ᴛᴏ ɪɴᴠɪᴛᴇ ʜᴇʀ (ᴜɴғᴏʀᴛᴜɴᴀᴛᴇʟʏ ᴛʜᴇ ᴜsᴇʀʙᴏᴛ ᴡɪʟʟ ᴊᴏɪɴᴇᴅ ʙʏ ɪᴛsᴇʟғ ᴡʜᴇɴ ʏᴏᴜ ᴛʏᴘᴇ `/play (sᴏɴɢ ɴᴀᴍᴇ)` ᴏʀ `/vplay (sᴏɴɢ ɴᴀᴍᴇ)`).
𝟺.) ᴛᴜʀɴ ᴏɴ/start ᴛʜᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ғɪʀsᴛ ʙᴇғᴏʀᴇ sᴛᴀʀᴛ ᴛᴏ ᴘʟᴀʏ ᴠɪᴅᴇᴏ/music.

`- END, EVERYTHING HAS BEEN SETUP -`

😘 ɪғ ᴛʜᴇ ᴜsᴇʀʙᴏᴛ ɴᴏᴛ ᴊᴏɪɴᴇᴅ ᴛᴏ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ, ᴍᴀᴋᴇ sᴜʀᴇ ɪғ ᴛʜᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ᴀʟʀᴇᴀᴅʏ ᴛᴜʀɴᴇᴅ ᴏɴ ᴀɴᴅ ᴛʜᴇ ᴜsᴇʀʙᴏᴛ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.

💘 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀ ғᴏʟʟᴏᴡ-ᴜᴘ ǫᴜᴇsᴛɪᴏɴs ᴀʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ ᴛᴇʟʟ ɪᴛ ᴏɴ ᴍʏ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ʜᴇʀᴇ: @{GROUP_SUPPORT}.""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◁", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""✨ **ʜᴇʟʟᴏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» ᴄʜᴏᴏsᴇ ᴛʜᴇ ᴍᴇɴᴜ ʙᴇʟᴏᴡ ᴛᴏ ʀᴇᴀᴅ ᴛʜᴇ ᴇxᴘʟᴀɴᴀᴛɪᴏɴ & sᴇᴇ ᴛʜᴇ ʟɪsᴛ ᴏғ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs !

😘 __ᴘᴏᴡᴇʀᴇᴅ ʙʏ {BOT_NAME} ᴘʀᴇsᴇɴᴛs🎁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("😊ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs 😊", callback_data="cbadmin"),
                    InlineKeyboardButton("😍 sᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅs 😇", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("😝 ʀᴇᴛᴜʀɴ ᴛᴏ ʜᴏᴍᴇ 😊", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("◁", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""🙄 ʜᴇʀᴇ ɪs ᴛʜᴇ ʙᴀsɪᴄ ᴄᴏᴍᴍᴀɴᴅs:

» /play (sᴏɴɢ ɴᴀᴍᴇ/ʟɪɴᴋ) - ᴘʟᴀʏ ᴍᴜsɪᴄ ᴏɴ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ
» /vplay (ᴠɪᴅᴇᴏ ɴᴀᴍᴇ/ʟɪɴᴋ) - ᴘʟᴀʏ ᴠɪᴅᴇᴏ ᴏɴ ᴠɪᴅᴇᴏ ᴄʜᴀᴛ
» /vstream - ᴘʟᴀʏ ʟɪᴠᴇ ᴠɪᴅᴇᴏ ғʀᴏᴍ ʏᴛ ʟɪᴠᴇ/ᴍ𝟹ᴜ𝟾
» /playlist - sʜᴏᴡ ʏᴏᴜ ᴛʜᴇ ᴘʟᴀʏʟɪsᴛ
» /video (ǫᴜᴇʀʏ) - ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ
» /song (ǫᴜᴇʀʏ) - ᴅᴏᴡɴʟᴏᴀᴅ sᴏɴɢ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ
» /lyric (ǫᴜᴇʀʏ) - sᴄʀᴀᴘ ᴛʜᴇ sᴏɴɢ ʟʏʀɪᴄ
» /search (ǫᴜᴇʀʏ) - sᴇᴀʀᴄʜ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ʟɪɴᴋ

» /ping - sʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴘɪɴɢ sᴛᴀᴛᴜs
» /uptime - sʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ sᴛᴀᴛᴜs
» /alive - sʜᴏᴡ ᴛʜᴇ ʙᴏᴛ ᴀʟɪᴠᴇ ɪɴғᴏ (ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ)

💘 ᴘᴏᴡᴇʀᴇᴅ ʙʏ: {BOT_NAME} ᴘʀᴇsᴇɴᴛs 🎁""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◁", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("admin commands")
    await query.edit_message_text(
        f"""🤎 ʜᴇʀᴇ ɪs ᴛʜᴇ ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs:

» /pause - ᴘᴀᴜsᴇ ᴛʜᴇ sᴛʀᴇᴀᴍ
» /resume - ʀᴇsᴜᴍᴇ ᴛʜᴇ sᴛʀᴇᴀᴍ
» /skip - sᴡɪᴛᴄʜ ᴛᴏ ɴᴇxᴛ sᴛʀᴇᴀᴍ
» /stop - sᴛᴏᴘ ᴛʜᴇ sᴛʀᴇᴀᴍɪɴɢ
» /vmute - ᴍᴜᴛᴇ ᴛʜᴇ ᴜsᴇʀʙᴏᴛ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ
» /vunmute - ᴜɴᴍᴜᴛᴇ ᴛʜᴇ ᴜsᴇʀʙᴏᴛ ᴏɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ
» /volume `𝟷-𝟸𝟶𝟶` - ᴀᴅᴊᴜsᴛ ᴛʜᴇ ᴠᴏʟᴜᴍᴇ ᴏғ ᴍᴜsɪᴄ (ᴜsᴇʀʙᴏᴛ ᴍᴜsᴛ ʙᴇ ᴀᴅᴍɪɴ)
» /reload - ʀᴇʟᴏᴀᴅ ʙᴏᴛ ᴀɴᴅ ʀᴇғʀᴇsʜ ᴛʜᴇ ᴀᴅᴍɪɴ ᴅᴀᴛᴀ
» /userbotjoin - ɪɴᴠɪᴛᴇ ᴛʜᴇ ᴜsᴇʀʙᴏᴛ ᴛᴏ ᴊᴏɪɴ ɢʀᴏᴜᴘ
» /userbotleave - ᴏʀᴅᴇʀ ᴜsᴇʀʙᴏᴛ ᴛᴏ ʟᴇᴀᴠᴇ ғʀᴏᴍ ɢʀᴏᴜᴘ

💘 ᴘᴏᴡᴇʀᴇᴅ ʙʏ: {BOT_NAME} ᴘʀᴇsᴇɴᴛs""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◁", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.answer("sudo commands")
    await query.edit_message_text(
        f"""💝 ʜᴇʀᴇ ɪs ᴛʜᴇ sᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅs:

» /gban (`ᴜsᴇʀɴᴀᴍᴇ` ᴏʀ `ᴜsᴇʀ ɪᴅ`) - ғᴏʀ ɢʟᴏʙᴀʟ ʙᴀɴɴᴇᴅ ᴘᴇᴏᴘʟᴇ
» /ungban (`ᴜsᴇʀɴᴀᴍᴇ` ᴏʀ `ᴜsᴇʀ ɪᴅ`) - ғᴏʀ ᴜɴ-ɢʟᴏʙᴀʟ ʙᴀɴɴᴇᴅ ᴘᴇᴏᴘʟᴇ
» /speedtest - ʀᴜɴ ᴛʜᴇ ʙᴏᴛ sᴇʀᴠᴇʀ sᴘᴇᴇᴅᴛᴇsᴛ
» /sysinfo - sʜᴏᴡ ᴛʜᴇ sʏsᴛᴇᴍ ɪɴғᴏʀᴍᴀᴛɪᴏɴ
» /update - ᴜᴘᴅᴀᴛᴇ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏ ʟᴀᴛᴇsᴛ ᴠᴇʀsɪᴏɴ
» /restart - ʀᴇsᴛᴀʀᴛ ʏᴏᴜʀ ʙᴏᴛ
» /leaveall - ᴏʀᴅᴇʀ ᴜsᴇʀʙᴏᴛ ᴛᴏ ʟᴇᴀᴠᴇ ғʀᴏᴍ ᴀʟʟ ɢʀᴏᴜᴘ
» /leavebot (`ᴄʜᴀᴛ ɪᴅ`) - ᴏʀᴅᴇʀ ʙᴏᴛ ᴛᴏ ʟᴇᴀᴠᴇ ғʀᴏᴍ ᴛʜᴇ ɢʀᴏᴜᴘ ʏᴏᴜ sᴘᴇᴄɪғʏ

» /eval - ᴇxᴇᴄᴜᴛᴇ ᴀɴʏ ᴄᴏᴅᴇ
» /sh - ʀᴜɴ ᴀɴʏ ᴄᴏᴍᴍᴀɴᴅ

» /broadcast (`ᴍᴇssᴀɢᴇ`) - sᴇɴᴅ ᴀ ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ɢʀᴏᴜᴘs ᴇɴᴛᴇʀᴇᴅ ʙʏ ʙᴏᴛ
» /broadcast_pin (`ᴍᴇssᴀɢᴇ`) - sᴇɴᴅ ᴀ ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴀʟʟ ɢʀᴏᴜᴘs ᴇɴᴛᴇʀᴇᴅ ʙʏ ʙᴏᴛ ᴡɪᴛʜ ᴛʜᴇ ᴄʜᴀᴛ ᴘɪɴ

😘 ᴘᴏᴡᴇʀᴇᴅ ʙʏ: {GROUP_NAME} ᴀɪ__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("◁", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 Only admin with manage video chat permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    chat = query.message.chat.title
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **Settings of** {chat}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(buttons),
          )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("❗ Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.message.delete()
