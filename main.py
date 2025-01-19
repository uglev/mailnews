import os
import telebot
from dotenv import find_dotenv, load_dotenv, set_key
import asyncio
from googletrans import Translator
import feedparser

dotenv_file = find_dotenv()
load_dotenv(dotenv_file)

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
RSS_UK = os.getenv('RSS_UK')
ID_MESSAGE = int(os.getenv('ID_MESSAGE'))
KEYWORDS = os.getenv('KEYWORDS')
database = []
result = ''
count_res = 0

bot = telebot.TeleBot(token=TELEGRAM_TOKEN)

def send_message(message):
    if ID_MESSAGE != 0:
        bot.delete_message(chat_id=CHAT_ID, message_id=ID_MESSAGE)
    new_id_message = bot.send_message(chat_id=CHAT_ID, text=message)
    set_key(dotenv_file, 'ID_MESSAGE', str(new_id_message.id))

def verify(array):
    for k in KEYWORDS.split():  # нужные слова
        for i in array:
            if k.lower() in i.lower():
                return array[0] + '\n' + array[2] + '\n'
    return False

def double(arr, url):
    for i in arr:
        if url in i:
            return False
    return True 

async def translate_text(text):
    async with Translator() as translator:
        result = await translator.translate(text, src='en', dest='ru')
        return result.text

goto = False
for rss_url in RSS_UK.split(', '):
    if result.count('\n') >= 9:
        break
    parsed = feedparser.parse(rss_url)
    for entry in parsed.entries:
        name = asyncio.run(translate_text(entry.title))
        desc = asyncio.run(translate_text(entry.description))
        url = entry.link
        res = verify([name, desc, url])
        if res != False:
            if double(result, url):
                result += res
if len(result) == 0:
    send_message('Сегодня интересных новостей нет! До завтра!')
else:
    send_message('Представляю интересные новости на сегодня:\n' + result)

