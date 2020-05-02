import telebot
import math_classes

BotTOKEN = '1196012818:AAFXZQMHfArrsGXQyxfgTAPasDOL15REKGA'
bot = telebot.TeleBot(BotTOKEN)


pi = 3.141592653589793238462643


@bot.message_handler(content_types=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, text='Я могу посчитать простое выражение')


@bot.message_handler(commands=['calc'])
def weather_message(message):
    bot.send_message(message.chat.id, text='Введите запрос в формате:'
                                           '\n4 + 5'
                                            '\nsin(20)')


if __name__ == '__main__':
    bot.polling()