from aiogram import Bot, Dispatcher, types
from aiogram.handlers import MessageHandler
from aiogram.filters import Command
from aiogram.types.web_app_info import WebAppInfo
import asyncio
import logging

APP_TOKEN = '6490619734:AAFCVV3I1Xadk8HaoXUnX4QSoWzqd-v3Rqs'
bot = Bot(APP_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)


@dp.message(Command('start'))
async def start(message: types.Message):
    kb = [
        [types.KeyboardButton(text='Открыть Сайтик', resize_keyboard=True,
                              web_app=WebAppInfo(url='https://0b45-5-18-144-205.ngrok-free.app'))]
    ]
    markup = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('Привет, все на сайте', reply_markup=markup)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
