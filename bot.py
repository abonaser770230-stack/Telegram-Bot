from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests, os
from bs4 import BeautifulSoup

TOKEN = os.getenv("TOKEN") # مهم: بياخذه من Koyeb

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبا بك في بوت سهيل للكتب 📚\nارسل اسم الكتاب")

async def search_book(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    await update.message.reply_text(f"جاري البحث عن: {query} ... ⏳")
    # نفس الكود اللي فوق
    # ... 

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_book))
app.run_polling()

