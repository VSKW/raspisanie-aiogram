from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import token
from aiogram.dispatcher.filters.state import State, StatesGroup




#Память
stor = MemoryStorage
#Создание бота и диспетчера
bot = Bot(token)
dp = Dispatcher(bot, storage=stor())

