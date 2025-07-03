import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import random

# গালি শব্দের তালিকা
bad_words = ['gandu', 'choda', 'bokachoda', 'madarchod', 'fuck', 'shit', 'banchod', 'চোদা', 'মাদারচোদ', 'চুদি']

# মজার র্যান্ডম reply
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

# Emoji reactions
reactions = ["❤️", "😂", "🔥", "😳", "🥰", "👍"]

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if msg and msg.text:
        text = msg.text.lower()

        # গালি চেক করে মুছে ফেলা
        if any(bad_word in text for bad_word in bad_words):
            try:
                await msg.delete()
                await msg.reply_text("ভাই গালি দিলে কিন্তু চলবে না 😠")
            except Exception as e:
                print("Delete failed:", e)
            return

        reply = random.choice(witty_replies)
        emoji = random.choice(reactions)
        await msg.reply_text(f"{reply} {emoji}")

async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🙋‍♂️ আমি XR GPT BOT! আপনার Bangla Group-এর অটো রিপ্লাই বন্ধু 🤖")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(\"""
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
\""")

async def about_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 XR GPT BOT তৈরি করেছে ChatGPT ভাইয়ের মতো একজন মিয়া 🧠")

async def owner_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👤 Bot Owner: @Xr_bd_bot")

def main():
    TOKEN = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start_cmd))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("about", about_cmd))
    app.add_handler(CommandHandler("owner", owner_cmd))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), auto_reply))
    app.run_polling()

if __name__ == "__main__":
    main()
