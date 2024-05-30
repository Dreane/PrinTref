from aiogram import Router
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я Печатник! Если вы хотите что-то распечатать, то нужно обратиться к Печатнику."
                         "Я печатаю для общежития ул.Трефолева д.1 и для вуза СПБГУТ.")

@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")