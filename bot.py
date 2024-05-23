import telebot
import datetime

bot = telebot.TeleBot('your token', parse_mode=None)
enemy_text = 'youtube.com/shorts'
current_date = datetime.datetime.now()

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Система 'Анти шортсы' - активировано!")

@bot.message_handler(func=lambda message: message.text.lower() == 'привет')
def send_hello(message):
	bot.send_message(message.chat.id, 'Привет')

@bot.message_handler(func=lambda message: message.text.lower() == 'пока')
def send_hello(message):
	bot.send_message(message.chat.id, 'Пока')

@bot.message_handler(func=lambda message: enemy_text in message.text)
def delete_shorts(message):
	bot.delete_message(message.chat.id, message.message_id)
	print(current_date, ' Удалён шортс - ', message.text)
	bot.send_message(message.chat.id, 'ПОПЫТКА СКИНУТЬ ШОРТС ПРЕДОТВРАЩЕНА')

bot.polling()
