from telegram.ext import Application
from app.config import settings
from app.telegram.handlers import register_handlers

def build_bot():
    app=Application.builder().token(settings.telegram_bot_token).build()
    register_handlers(app)
    return app
