# app.py

import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from deep_translator import GoogleTranslator
import pykakasi
import asyncio

# Ambil token dari environment (Render.com)
TOKEN = os.getenv("BOT_TOKEN")

# Inisialisasi converter romaji
kks = pykakasi.kakasi()

def to_romaji(text: str) -> str:
    result = kks.convert(text)
    return " ".join([item["hepburn"] for item in result])

async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    original = update.message.text
    jp = GoogleTranslator(source="auto", target="ja").translate(original)
    romaji = to_romaji(jp)
    reply = f"🇯🇵 {jp}\n📝 {romaji}"
    await update.message.reply_text(reply)

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), translate))
    
    print("Bot is running...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
