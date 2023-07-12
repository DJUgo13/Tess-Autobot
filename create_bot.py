from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import decouple


API_TOKEN = '6266033622:AAGUMkWcATHXAm7h9CvmIloydZfV2FM4A9g'
Chat_id = "" # Чат, куда будут приходить заявки


bot = Bot(token=API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
