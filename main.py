from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token(
    "5683673903:AAE0_sgK3snWaUVLSPwFcD61B2WGQVPx6jo").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("doll", doll_command))
app.add_handler(CommandHandler("news", news_command))
app.add_handler(CommandHandler("weat", weat_command))

print('start server')
app.run_polling()
