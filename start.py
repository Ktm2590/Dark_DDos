import sys, os, telebot
from threading import Timer
import re
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from core.colors import *
from core.setting import *
from core.banner import *
from start import *
from core import update
os.system('figlet Dark_DDos')
print('')
print(banner)
print('')

def main():
    global id
    global token
    var = input(B + '[cb]' + R + '>>> ' + W)
    if 'set token' in var.lower():
        var1 = var.split(' ')
        token = var1[2]
        print(G + '\nТокен успешно установлен\n' + W)
        main()
    elif 'set id' in var.lower():
        var2 = var.split(' ')
        id = var2[2]
        print(G + '\nАйди успешно установлено\n' + W)
        main()
    elif var == 'help':
        print('\nЧто бы создать бота перейдите к @BotFather, и создайте нового бота, после этого напишите команду set token (токен от вашего бота), а так же set id (ваш айди).\n')
        main()
    elif var == 'show options':
        try:
            print(f"\noptions or bots\n===============\n\ntoken>>{token}\nid>>{id}\n")
        except:
            print('\noptions or bots\n===============\n\ntoken>>nome\nid>>none\n')

        main()
    elif var == 'start':
        os.system(f"cd core; python3 bot.py {token} {id}")
    else:
        print(R + '\nНеверная команда! Для справки напишите help\n' + W)
        main()


main()
if __name__ == '__main__':
    bot.polling(none_stop=True)