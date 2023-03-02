from telebot.async_telebot import AsyncTeleBot
from aiogram import executor, Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
TOKEN_API = "1907377326:AAGMcAXgLCLfWlgrAJZhSryFxiPgAKIi_zQ"

storage = MemoryStorage()
bot = Bot(TOKEN_API)
dp = Dispatcher(bot=bot,
                storage =storage)

def get_keyboard()->ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("Start working"))

    return kb

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await message.answer("Welcome",
                         reply_markup=get_keyboard())

print("Changes were done by Zolto")
