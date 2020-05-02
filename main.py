import telebot
import math_classes
import math

BotNAME = 'EngineeringCalculator'
BotTOKEN = '1196012818:AAFXZQMHfArrsGXQyxfgTAPasDOL15REKGA'
bot = telebot.TeleBot(BotTOKEN)


@bot.message_handler(content_types=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, text='Я могу посчитать простое выражение')


@bot.message_handler(commands=['eval'])
def weather_message(message):
    bot.send_message(message.chat.id, text='Введите запрос в формате:'
                                           '\n4 + 5'
                                            '\nsin(20)'
                                            '\n 3 ^ (4 / 2)')


@bot.message_handler(content_types=["text"])
def calculator_logic(message):
    text = message.text
    bot.send_message(message.chat.id, math_classes.parse(text))


if __name__ == '__main__':
    bot.polling()