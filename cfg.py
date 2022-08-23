token = '1399562656:AAEQrQhhaBgb6d5eLZRrrqVKPlsI-7qkH9Y'

def keyboard1():
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text='Регистрация', callback_data='reg'))
	markup.add(types.InlineKeyboardButton(text='Как работает бот?', callback_data='how'))
	markup.add(types.InlineKeyboardButton(text='Начать подбор машины', callback_data='car'))

