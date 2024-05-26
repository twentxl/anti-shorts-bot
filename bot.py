import telebot
import datetime

bot = telebot.TeleBot('your token', parse_mode=None)
enemy_text = 'youtube.com/shorts'

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
	current_date = datetime.datetime.now()
	user_name = message.from_user.username
	
	bot.delete_message(message.chat.id, message.message_id)
	print(current_date, f' {user_name} Удалён шортс - ', message.text)
	bot.send_message(message.chat.id, 'ПОПЫТКА СКИНУТЬ ШОРТС ПРЕДОТВРАЩЕНА')

print('Бот запущен')
bot.polling()
