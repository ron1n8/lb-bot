import datetime


class Config:
	def __init__(self):
		self.TOKEN = '2023199506:AAExb6Ne1RburJg970UOSKz8YXDXOedB3AI'
		self.SERVER_TOKEN = ''
		self.log_file = open('log.txt', 'a')


	def logg(self, message, level = 3, sep = False):
		if sep:
			print('\n\n')
			self.log_file.write('\n\n')

		if level == 1:
			self.log_file.write(f'[!] {message} || {datetime.datetime.now()}')
			print(f'[!] {message}')
		elif level == 2:
			self.log_file.write(f'[#] {message} || {datetime.datetime.now()}')
			print(f'[#] {message}')
		else:
			# self.log_file.write(f'[+] {message} || {datetime.datetime.now()}')
			print(f'[+] {message}')



	def getName(self, inline_set, key):
		for name_set in inline_set:
			for name in name_set:
				if name.callback_data == key:
					return name.text


	def safer(self, func):
		try:
			func()
		except Exception as e:
			self.logg(e, 1)




def buildOrder(data, user):
	final = {
		'order': data,
		'cname': user['name'],
		'phone': '+'+user['contact'],
		'location': user['location'],
		'id': user['id'],
		'username': '@'+user['username']
	}

	return final


def buildUser(message):
	user = dict()
	user['id'] = message['from'].id
	user['username'] = message['from'].username
	user['name'] = message['from'].first_name
	user['location'] = dict()
	user['contact'] = str()

	if user['username'] is None:
		user['username'] = 'empty'

	return user


def makeUser(message):
	user = list()
	user.append(message['from'].id)
	if message['from'].username == None:
		user.append('empty')
	else:
		user.append(message['from'].username)
	user.append(message['from'].first_name)
	user.append(message.contact.phone_number)
	user.append(str())
	user.append(str())

	return user

config = Config()