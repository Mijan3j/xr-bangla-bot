import os
import random
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# গালি শব্দের তালিকা (আপনি প্রয়োজনমতো বাড়াতে পারেন)
bad_words = [
    'gandu', 'choda', 'bokachoda', 'madarchod', 'fuck', 'shit', 'banchod',
    'চোদা', 'মাদারচোদ', 'চুদি'
]

# witty Bangla reply গুলো
witty_replies = [
    "কি কইলেন মিয়া! একদম বাজিমাত 😎",
    "এইটা বলার দরকার ছিল ভাই? 😅",
    "আজকে কইরা দিলেন ভাই! 🔥",
    "আপনার কথায় ফাটাফাটি vibe পাইছি! 🤩",
    "এমন কথা শুনে চা খাইতে মন চাইতেছে ☕",
    "ভাই, এমন reply কই পাইলেন! 😂",
    "মনে হচ্ছে আপনি heavy জিনিস! 🧠",
    "এইরকম কথা শুনলে bot ও মজা পায়! 🤖",
    "ভাই, কথা কম কিন্তু meaning deep! 🧐",
    "Telegram group ভাই ভাই — আপনি রাজা! 👑"
]

# Emoji reactions (যদি দরকার হয়)
reactions = ["❤️", "😂", "🔥", "😳", "🥰", "👍"]


async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🙋‍♂️ আমি XR GPT BOT! আপনার Bangla Group-এর অটো রিপ্লাই বন্ধু 🤖\n"
        "সাহায্যের জন্য /help টাইপ করুন।"
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
📚 সাহায্যের তালিকা:
✅ Random Bangla auto-reply
✅ গালি দিলে auto delete
✅ Stylish witty ChatGPT-style response
✅ Emoji react
✅ Commands:
/start - বট চালু করুন
/help - সাহায্য নিন
/about - বট সম্পর্কে জানুন
/owner - নির্মাতার সাথে যোগাযোগ
""")


async def about_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 XR GPT BOT তৈরি করেছে ChatGPT ভাইয়ের মতো একজন মিয়া 🧠"
    )


async def owner_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👤 Bot Owner: @Xr_bd_bot"
    )


async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if msg and msg.text:
        text = msg.text.lower()

        # গালি চেক করে মুছে ফেলা
        if any(bad_word in text for bad_word in bad_words):
            try:
                await msg.delete()
                return  # গালি পেলে reply দিবে না
            except Exception as e:
                print("Delete failed:", e)
                return

        # নরমাল মেসেজে witty reply
        reply = random.choice(witty_replies)
        emoji = random.choice(reactions)
        await msg.reply_text(f"{reply} {emoji}")


def main():
    TOKEN = os.getenv("BOT_TOKEN")
    if not TOKEN:
        print("Error: BOT_TOKEN environment variable missing!")
        return

    app = ApplicationBuilder().token(TOKEN).build()

    # Command handlers
    app.add_handler(CommandHandler("start", start_cmd))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("about", about_cmd))
    app.add_handler(CommandHandler("owner", owner_cmd))

    # Message handler (auto reply & bad word delete)
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), auto_reply))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
