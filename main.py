from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json

bot = Bot('6448669823:AAG5yiZrIDrNTp7kdsor4zH8hv3nzClJVDI')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton(
        'Открыть веб-страницу', web_app=WebAppInfo(url='https://roflerboom.github.io/willberries/tg-buy.html')))
    await message.answer('привет мой друг', reply_markup=markup)


@dp.message_handler(content_types=['wev_app_data'])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Name:{res["name"]}, email:{res["email"]}, phone: {res["phone"]}')

executor.start_polling(dp)
