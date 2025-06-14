from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from deep_translator import GoogleTranslator
import pykakasi
import os

TOKEN = os.getenv(8146298227:AAEFZdSt7tEKqr4Gg-dZHLJSF-2AAvEhyMk)

kks = pykakasi.kakasi()

def to_romaji(japanese_text):
    result = kks.convert(japanese_text)
    return ' '.join([item['hepburn'] for item in result])

async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    jp_text = GoogleTranslator(source='en', target='ja').translate(text)
    romaji = to_romaji(jp_text)
    await update.message.reply_text(f"🇯🇵 {jp_text}\n📝 {romaji}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), translate))
    print("Bot is running...")
    app.run_polling()
