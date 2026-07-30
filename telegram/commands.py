from telegram import Update
from telegram.ext import ContextTypes
from app.telegram.messages import START_MESSAGE
from app.telegram.menus import main_keyboard

async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(START_MESSAGE,reply_markup=main_keyboard())
