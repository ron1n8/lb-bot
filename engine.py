import config
import webhook

from aiogram import Bot, Dispatcher, executor, types




class TeleBot:

	bot = Bot(token = config.config.TOKEN)
	dispatch = Dispatcher(bot)


	def __init__(self):
		self.server = webhook.Server()

	@dispatch.message_handler(commands = ['start', 'help'])
	async def greet(message):
		print(message)
		await message.reply('Hello')



	@dispatch.message_handler()
	async def default_answer(message):
		print('\n\n')
		print(message)


		markup = types.ReplyKeyboardMarkup()
		markup.add(types.KeyboardButton('Button'))
		await message.answer(message.text, reply_markup = markup)


if __name__ == '__main__':
	bot = TeleBot()
	executor.start_polling(bot.dispatch, skip_updates = True)