from env import MUST_JOIN
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
#    if not MUST_JOIN:
#        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"Si Anjeng, Masuk Sini Dulu Lu Bangsat !",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("Sini Nyet Masuk, Jangan Lupa Salam", url=link)]
                    ])
                )
            except UserBannedInChannel:
                await bot.send_message(
                msg.chat.id,
                "**Maaf, Anda tidak dapat menggunakan bot ini karena anda di banned dari Kynan Support**\n**Silakan contact @Rizzvbss agar dibuka blokir anda.**"
            )
    except ChatAdminRequired:
        print(f"I'm not admin in the MUST_JOIN chat : {MUST_JOIN} !")