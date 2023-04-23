from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
text_task_input = False
image_task_input = False


keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(types.KeyboardButton('Текст'))
keyboard.add(types.KeyboardButton('Изображение'))