from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.inline import games_inline_keyboard

common_router= Router()




@common_router.message(Command(commands=['start']))  # Берём только сообщения, являющиеся командой /start
async def start_command(message: Message):  # message - сообщение, которое прошло через фильтр
    await message.answer("Привет!выбери игру,в которую хочешь сыграть+_+",
                         reply_markup=games_inline_keyboard)