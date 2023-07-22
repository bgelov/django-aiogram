from aiogram.contrib.fsm_storage.memory import MemoryStorage

from ruargbot.settings import TELEGRAM_BOT_TOKEN
from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.fsm_storage.redis import RedisStorage2


bot = Bot(token=TELEGRAM_BOT_TOKEN, parse_mode=types.ParseMode.HTML)
# storage = RedisStorage2()
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)
dp = Dispatcher(bot)