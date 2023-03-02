from telebot.async_telebot import AsyncTeleBot
from aiogram import executor, Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
TOKEN_API = "sd"

storage = MemoryStorage()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot=bot,
                storage =storage)

print("Changes were done by Zolto")
