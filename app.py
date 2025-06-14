import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from deep_translator import GoogleTranslator
import pykakasi

TOKEN = os.getenv("BOT_TOKEN")
kks = pykakasi.kakasi()

def to_romaji(text):
    return " ".join([item["hepburn"] for item in kks.convert(text)])

async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    jp_text = GoogleTranslator(source="auto", target="ja").translate(text)
    romaji = to_romaji(jp_text)
    await update.message.reply_text(f"🇯🇵 {jp_text}\n📝 {romaji}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), translate))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
