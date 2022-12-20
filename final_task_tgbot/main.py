import telebot
import requests
import pytz
import datetime

bot = telebot.TeleBot("5842701010:AAHH8i9ZgJ9lmIBKP1MinstnnpMKu2Vk5EY")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Create a keyboard with three buttons
    markup = telebot.types.ReplyKeyboardMarkup(row_width=3)
    markup.add(telebot.types.KeyboardButton('Time in Moscow'), telebot.types.KeyboardButton('Time in Buenos Aires'), telebot.types.KeyboardButton('USD Exchange Rate (CBR)'))
    bot.send_message(message.chat.id, "Welcome! Please choose an option:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Time in Moscow')
def time_in_moscow(message):
    # Get the current time in Moscow
    tz = pytz.timezone('Europe/Moscow')
    current_time = datetime.datetime.now(tz)
    bot.send_message(message.chat.id, f'The current time in Moscow is {current_time.strftime("%H:%M:%S")}')

@bot.message_handler(func=lambda message: message.text == 'Time in Buenos Aires')
def time_in_buenos_aires(message):
    # Get the current time in Buenos Aires
    tz = pytz.timezone('America/Buenos_Aires')
    current_time = datetime.datetime.now(tz)
    bot.send_message(message.chat.id, f'The current time in Buenos Aires is {current_time.strftime("%H:%M:%S")}')

@bot.message_handler(func=lambda message: message.text == 'USD Exchange Rate (CBR)')
def usd_exchange_rate(message):
    # Scrape the current exchange rate of the US Dollar from the Central Bank of Russia's website
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = response.json()
    rate_usd = data['Valute']['USD']['Value']
    # Отправляем сообщение с курсом евро пользователю
    bot.send_message(message.chat.id, f'Курс доллара: {rate_usd:.2f} руб.')  

bot.polling()
