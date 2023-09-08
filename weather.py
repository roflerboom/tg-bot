import telebot
import requests
import json

bot = telebot.TeleBot('6448669823:AAG5yiZrIDrNTp7kdsor4zH8hv3nzClJVDI')
API = 'abee9796a740914ece3366a6f2860a40'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, 'Напиши город, в котором хочешь узнать погоду')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp}°')

        image = 'sunny.png' if temp > 5.0 else 'sun.png'
        file = open('./images/' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Город указан не верно')


bot.polling(non_stop=True)
