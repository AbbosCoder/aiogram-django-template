from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from asgiref.sync import sync_to_async
from robot.models import TelegramUser
from loader import dp
import logging


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_name=message.from_user.username
    
    try:    
        telegram_user, _ = await TelegramUser.objects.aget_or_create(
            full_name=message.from_user.full_name,
            username=user_name,
            user_id=message.from_user.id,
        )
    except:
        telegram_user, _ = await TelegramUser.objects.aget_or_create(
            full_name=message.from_user.full_name,
            username='Mavjud emas',
            user_id=message.from_user.id,
        )

    logging.info("New user")
    await message.answer(f"Salom, {message.from_user.full_name}!")
