# from aiogram import Bot, Dispatcher, executor, types

# bot = Bot('6448669823:AAG5yiZrIDrNTp7kdsor4zH8hv3nzClJVDI')
# dp = Dispatcher(bot)


# @dp.message_handler(commands=['photo'])
# async def start(message: types.Message):
#     # await bot.send_message(message.chat.id, 'hello')
#     # await message.answer('hello')
#     await message.reply('hello')


# @dp.message_handler(commands=['inline'])
# async def info(message: types.Message):
#     markup = types.InlineKeyboardMarkup(row_width=2)
#     markup.add(types.InlineKeyboardButton('Sita', url='www.google.com'))
#     markup.add(types.InlineKeyboardButton('hello', callback_data='hello'))
#     await message.reply('hello', reply_markup=markup)


# @dp.callback_query_handler()
# async def callback(call):
#     await call.message.answer(call.data)


# @dp.message_handler(commands=['reply'])
# async def reply(message: types.Message):
#     markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
#     markup.add(types.KeyboardButton('Site'))
#     markup.add(types.KeyboardButton('Website'))
#     await message.answer('Hello reply', reply_markup=markup)
# executor.start_polling(dp)
