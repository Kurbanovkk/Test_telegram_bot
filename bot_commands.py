from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from bs4 import BeautifulSoup as bs


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!!!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hi\n/help\n/doll\n/weat\n/news')


async def doll_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = ('https://cbr.ru/')
    response = requests.get(url).text
    soup = bs(response, 'html.parser')
    doll = soup.find('div', class_="col-md-2 col-xs-9 _right mono-num")
    await update.message.reply_text(f'Курс доллара на сегодняшний день = {doll.text}')


async def weat_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url_1 = ('https://world-weather.ru/pogoda/russia/makhachkala/')
    response_1 = requests.get(url_1).text
    soup_1 = bs(response_1, 'html.parser')
    weat = soup_1.find('div', id="weather-now-number")
    await update.message.reply_text(f'погода в Махачкале днем {weat.text}')


async def news_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url_2 = ('https://www.rbc.ru/')
    response_2 = requests.get(url_2).text
    soup_2 = bs(response_2, 'html.parser')
    news = soup_2.find('span', class_="main__big__title")
    await update.message.reply_text(f'Главная новость на сегодня:  {news.text}')
