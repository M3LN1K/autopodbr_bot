import sqlite3

con = None

def get_con():
	global con
	if con is None:
		con = sqlite3.connect('telegbd.db3')
	return con

def init_db(force: boll = False):
	conn = get_con()

	cursor = conn.cursor()

	if force:
		cursor.execute('DROP TABLE IF EXISTS user')

	conn.commit()

def add_message(user_id: int, name: str, surename: str, nikname: str, phone: int, email: str, password: str, city: str)