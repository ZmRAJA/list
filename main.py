import os
from pyrogram import Client, filters
from pyrogram.errors import QueryIdInvalid
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InputTextMessageContent
from pyrogram.types import InlineQueryResultArticle


Bot = Client(
    "tgDonatebot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)


START_TEXT = """Hᴇʏ! {}
☞ Vᴇʀʏ Hᴀᴘᴘʏ ᴛᴏ Kɴᴏᴡ Tʜᴀᴛ Yᴏᴜ ᴀʀᴇ here to find Movies channle .
Tʜᴀɴᴋꜱ Fᴏʀ Uꜱɪɴɢ [Oᴜʀ Bᴏᴛꜱ](https://t.me/Latest_hindi_hd_Movies_Hub).
Mᴀᴅᴇ Wɪᴛʜ Lᴏᴠᴇ Fᴏʀ [Yᴏᴜ](tg://settings)"""

DONATE_BUTTONS = [
    InlineKeyboardButton(
        text='📥📥 MOVIES CHANNLE 📥📥 ',
        callback_data='donateme'
    )
]

DONATE_TEXT = """Hᴇʏ! {}
Yᴏᴜ Cᴀɴ JOIN LATEST MOVIES CHANNLE.
PayTm/PhonePe/GooglePay - `ABCD1234@okaxis`
Oʀ Cᴏɴᴛᴀcᴛ Uꜱ :- [ツowner 🇮🇳](https://t.me/DeltaBotsOfficial). """

BUTTON_TEXT = """ Click the Below Buttons To JOIN MOVIES CHANNLES. """

MOVIES_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(" Back ", callback_data="back"),
            InlineKeyboardButton(" ⭕️MOVIES⭕️ ", url="https://t.me/Latest_hindi_hd_Movies_Hub")
        ],
        [
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

PAY_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(" ⚡️MOVIES 1⚡️ ",url="https://t.me/Latest_hindi_hd_Movies_Hub"),
            InlineKeyboardButton(" 📥📥MOVIES 2 📥 ", url="https://t.me/Latest_hindi_hd_Movies_Hub")
        ],
        [
            InlineKeyboardButton(" ⚡️MOVIES 3⚡️ ",url="https://t.me/Latest_hindi_hd_Movies_Hub"),
            InlineKeyboardButton(" 📥📥MOVIES 📥 ", url="https://t.me/Latest_hindi_hd_Movies_Hub")
        ],
        [
            InlineKeyboardButton(" ⚡️MOVIES 4 ⚡️ ",url="https://t.me/Latest_hindi_hd_Movies_Hub"),
            InlineKeyboardButton(" 📥📥MOVIES 5📥 ", url="https://t.me/Latest_hindi_hd_Movies_Hub")
        ],
        [
            InlineKeyboardButton(" ⚡️MOVIES 6⚡️ ",url="https://t.me/Latest_hindi_hd_Movies_Hub"),
            InlineKeyboardButton(" 📥📥MOVIES 7📥 ", url="https://t.me/Latest_hindi_hd_Movies_Hub")
        ],
        [
            InlineKeyboardButton('Close', callback_data='close')
        ]
    ]
)

@Bot.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=InlineKeyboardMarkup([DONATE_BUTTONS]),
        disable_web_page_preview=True,
        quote=True
    )


@Bot.on_message(filters.private & filters.command(["donate"]))
async def donate(bot, update):
    await bot.send_message(
        text="Click the Following Button to Donate Us.",
        reply_markup=InlineKeyboardMarkup([PAY_BUTTONS]),
        disable_web_page_preview=True,
        quote=True
    )

@Bot.on_message(filters.private & filters.command(["bots"]))
async def bots(bot, update):
    await bot.send_message(
        text="https://t.me/Latest_hindi_hd_Movies_Hub",
        reply_markup=InlineKeyboardMarkup([PAY_BUTTONS]),
        disable_web_page_preview=True,
        quote=True
    )

@Bot.on_inline_query()
async def answerX(bot, update):

    answer = list()
    answer.append(InlineQueryResultArticle(title="This is My Donation Or Payment Bot", description="You Can Donate Us Using Inline.",
    input_message_content=InputTextMessageContent(message_text="Please donate us any amount you like, to support the services."),
    reply_markup=InlineKeyboardMarkup( [ [ InlineKeyboardButton("Dᴏɴᴀᴛᴇ 💳", url="") ] ] ),
    thumb_url="https://telegra.ph/file/330bd070950b8ef775ca9.jpg") )
    try:
        await update.answer(results=answer, cache_time=0)
    except Exception as e:
        print(f"🚸 ERROR : {e}")
    except QueryIdInvalid:
        pass

@Bot.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "donateme":
        await update.message.edit_text(
            text=BUTTON_TEXT.format(update.from_user.mention),
            reply_markup=PAY_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "upidata":
        await update.message.edit_text(
            text=DONATE_TEXT.format(update.from_user.mention),
            reply_markup=UPI_BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "back":
        await update.message.edit_text(
            text=BUTTON_TEXT.format(update.from_user.mention),
            reply_markup=PAY_BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()

Bot.run()
