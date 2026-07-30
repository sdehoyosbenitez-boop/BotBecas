from telegram.ext import CommandHandler
from app.telegram.commands import start

def register_handlers(app):
    app.add_handler(CommandHandler("start", start))
