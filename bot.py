import telebot
import datetime
import traceback

bot = telebot.TeleBot('TOKEN', parse_mode=None)
enemy_text = 'youtube.com'
edit_text = 'youtu.be'

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Система 'ANTI SHORTS' - активировано!")

@bot.message_handler(commands=['stop'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Ты долбаёб?")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	user_name = message.from_user.username
	if user_name == 'YOUR USERNAME':
		bot.send_message(message.chat.id, "Всё что угодно!")
	else:
		bot.send_message(message.chat.id, f"{user_name}, Ты долбаёб?")

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
	bot.send_message(message.chat.id, 'УБЕРИ ЭТУ ХУЙНЮ')

@bot.message_handler(func=lambda message: edit_text in message.text)
def delete_shorts(message):
	current_date = datetime.datetime.now()
	user_name = message.from_user.username

	bot.delete_message(message.chat.id, message.message_id)
	print(current_date, f' {user_name} Удалён шортс - ', message.text)
	bot.send_message(message.chat.id, 'УБЕРИ ЭТУ ХУЙНЮ')

@bot.edited_message_handler(func=lambda message: enemy_text in message.text)
def delete_edited_shorts(message):
	current_date = datetime.datetime.now()
	user_name = message.from_user.username

	bot.delete_message(message.chat.id, message.message_id)
	print(current_date, f' {user_name} Удалён шортс - ', message.text)
	bot.send_message(message.chat.id, 'УБЕРИ ЭТУ ХУЙНЮ')

@bot.edited_message_handler(func=lambda message: edit_text in message.text)
def delete_edited_shorts(message):
	current_date = datetime.datetime.now()
	user_name = message.from_user.username

	bot.delete_message(message.chat.id, message.message_id)
	print(current_date, f' {user_name} Удалён шортс - ', message.text)
	bot.send_message(message.chat.id, 'УБЕРИ ЭТУ ХУЙНЮ')

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
	current_date = datetime.datetime.now()
	user_name = message.from_user.username

	if user_name == 'Имя дурачка':
		bot.delete_message(message.chat.id, message.message_id)
		print(current_date, f' {user_name} Удалёна фотография')
		bot.send_message(message.chat.id, 'Не пройдешь!!!')

@bot.message_handler(content_types=['video'])
def handle_photo(message):
	current_date = datetime.datetime.now()
	user_name = message.from_user.username

	if user_name == 'Имя дурачка':
		bot.delete_message(message.chat.id, message.message_id)
		print(current_date, f' {user_name} Удалёно видео')
		bot.send_message(message.chat.id, 'Не пройдешь!!!')

try:
	print('Бот запущен\n')
	bot.polling()
except:
	traceback.print_exc()
