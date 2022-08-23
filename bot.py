import telebot
import cfg
import pymongo
import mysql.connector
from telebot import types
from pymongo import MongoClient
from mysql.connector import errorcode
from string import Template
from telegram import Bot
from telegram import Update
from telegram.utils.request import Request
from logging import getlogger



def main():
	req = Request(
		connect_timeout=0.5,
		read_timeout=1.0,
	)
	bot = Bot(
		token='1399562656:AAEQrQhhaBgb6d5eLZRrrqVKPlsI-7qkH9Y',
		request=req,
		base_url='https://telegg.ru/orig/bot',
	)
	update = Update(
		bot=bot,
		use_context=True,
	)

	info = bot.get_me()
	print(f'Bot info: {info}')
'''
bot = telebot.TeleBot(cfg.token)


  

@bot.message_handler(commands=['start'])
def start_message(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text='Показать команды', callback_data='help'))
	markup.add(types.InlineKeyboardButton(text='Как работает бот?', callback_data='how'))
	markup.add(types.InlineKeyboardButton(text='Начать подбор машины', callback_data='car'))
	bot.send_message(message.chat.id, text='''Доброго времени суток.\b 
		Позвольте представиться, я Drug.\b 
		Подбодбираю машины любых марок и расценок, 
		вам нужно лишь пройти небольшую регистрацию прямо здесь и указать критерии подбора машин для меня.\b 
		Ну что, приступим!''', reply_markup=markup)'''

'''
@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id,  '''1. /help - Выводит список комманд\b
										2. /start - Запускает бота\b
										3. /reg - Что бы зарегистрировать в боте (Обязательно)\b
										4. /about - Информация о боте и комманде разработчиков''')'''


# /about
#@bot.message_handler(commands=['about'])


# /reg
#@bot.message_handler(commands=["reg"])


	

'''
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

	bot.answer_callback_query(callback_query_id=call.id, text='Хороший выбор!')
	answer = ''
	if call.data == 'help':
		bot.send_message(call.message.chat.id, "Для того что бы посмотреть команды напиши команду /help ")
		bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
	elif call.data == 'how':
		answer = 'Смотри'
		bot.send_message(call.message.chat.id, answer)
		bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
	elif call.data == 'car':
		answer = 'Поехали.'
		bot.send_message(call.message.chat.id, answer)
		bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

'''

bot.polling(none_stop=False)


