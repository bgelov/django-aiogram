import asyncio
from datetime import timedelta

from aiogram.types import ChatPermissions
from django.utils import timezone
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from banbot.loader import dp, bot
from banbot.models import User, Chat


def sync_check_rights(admin_user):
    try:
        user = User.objects.get(chat_id=admin_user, can_mute_all=True)
        if user:
            chat_ids = Chat.objects.values_list('chat_id', flat=True)
            return set(chat_ids)
    except:
        return None

async def bot_muteall_x(message: types.Message, seconds):
    length = timedelta(seconds=seconds)
    reply_user_id = message.reply_to_message.from_user.id
    admin_user = str(message.from_id)
    # Получение текущего времени с учетом часового пояса Django
    now = timezone.now()

    # Добавляем заданное количество секунд к текущему времени
    ban_until = now + length

    chat_ids = await asyncio.to_thread(sync_check_rights, admin_user)

    for chat_id in chat_ids:
        await bot.restrict_chat_member(chat_id=chat_id,
                                       user_id=reply_user_id,
                                       permissions=ChatPermissions(can_send_messages=False),
                                       until_date=ban_until)
        # await message.answer(f"Пользователь id{ reply_user_id } получил muteall.")
    #else:
    #    await message.answer("Вы не можете выполнять данную команду.")


@dp.message_handler(Command('muteall1min'))
async def bot_muteall1min(message: types.Message):
    await bot_muteall_x(message, seconds=60)


@dp.message_handler(Command('muteall1d'))
async def bot_muteall1d(message: types.Message):
    await bot_muteall_x(message, seconds=86400)


@dp.message_handler(Command('muteall1w'))
async def bot_muteall1w(message: types.Message):
    await bot_muteall_x(message, seconds=604800)


@dp.message_handler(Command('muteall1m'))
async def bot_muteall1m(message: types.Message):
    await bot_muteall_x(message, seconds=2592000)
