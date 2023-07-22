import asyncio
from datetime import timedelta

from aiogram.types import ChatPermissions
from django.utils import timezone
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from banbot.loader import dp, bot
from banbot.models import User



def sync_check_rights(reply_user_id):
    try:
        user = User.objects.get(chat_id=reply_user_id, can_mute=True)
        return user is not None
    except User.DoesNotExist:
        return False

async def bot_mute_x(message: types.Message, seconds):
    length = timedelta(seconds=seconds)
    chat_id = message.chat.id
    reply_user_id = message.reply_to_message.from_user.id
    admin_user = message.from_id
    # Получение текущего времени с учетом часового пояса Django
    now = timezone.now()

    # Добавляем заданное количество секунд к текущему времени
    ban_until = now + length

    has_rights = await asyncio.to_thread(sync_check_rights, admin_user)

    if has_rights:
        await bot.restrict_chat_member(chat_id=chat_id,
                                       user_id=reply_user_id,
                                       permissions=ChatPermissions(can_send_messages=False),
                                       until_date=ban_until)
        # await message.answer(f"Пользователь id{ reply_user_id } получил mute.")
    #else:
    #    await message.answer("Вы не можете выполнять данную команду.")

@dp.message_handler(Command('mute1min'))
async def bot_mute1min(message: types.Message):
    await bot_mute_x(message, seconds=60)


@dp.message_handler(Command('mute1d'))
async def bot_mute1d(message: types.Message):
    await bot_mute_x(message, seconds=86400)


@dp.message_handler(Command('mute1w'))
async def bot_mute1w(message: types.Message):
    await bot_mute_x(message, seconds=604800)


@dp.message_handler(Command('mute1m'))
async def bot_mute1m(message: types.Message):
    await bot_mute_x(message, seconds=2592000)
