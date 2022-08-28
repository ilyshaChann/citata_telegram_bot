import requests
import logging
from aiogram import Bot, Dispatcher, executor, types
import menu_citata as menu

bot = Bot(token = '5313293532:AAEoposyAaTN82rPZB2YYfjawSP-oWEwzho')

dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=("start"))
async def send_hello(message: types.Message):
    await message.answer("Привет, друг, хочешь отправлю тебе случайную цитату?", reply_markup=menu.y)


@dp.message_handler(lambda message: message.text == "Нет.")
async def random_citata1(message: types.Message):
    await message.answer('Ну ладно, как знаешь...\nЕсли все-таки захочешь получить случайную цитатку, то набирай\n/start')

@dp.message_handler(lambda message: message.text == "Да!")
async def random_citata(message: types.Message):
    url = 'http://api.forismatic.com/api/1.0/'
    payload = {'method': 'getQuote', 'format': 'json', 'lang': 'ru'}
    res = requests.get(url, params=payload)
    data = res.json()
    text = data['quoteText']
    await message.answer('Держи :)\n' + text, parse_mode=None)


@dp.message_handler()
async def echo_text(message: types.Message):
    await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)