import asyncio
from datetime import timedelta
from django.utils import timezone
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from banbot.loader import dp, bot
from banbot.models import User



def sync_check_rights(reply_user_id):
    try:
        user = User.objects.get(chat_id=reply_user_id, can_ban=True)
        return user is not None
    except User.DoesNotExist:
        return False


async def bot_ban_x(message: types.Message, seconds):
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
        await bot.ban_chat_member(chat_id=chat_id, user_id=reply_user_id, until_date=ban_until)
        # await message.answer(f"Пользователь id{ reply_user_id } заблокирован.")
    #else:
    #    await message.answer("Вы не можете выполнять данную команду.")

@dp.message_handler(Command('ban1min'))
async def bot_ban1min(message: types.Message):
    await bot_ban_x(message, seconds=60)


@dp.message_handler(Command('ban1d'))
async def bot_ban1d(message: types.Message):
    await bot_ban_x(message, seconds=86400)


@dp.message_handler(Command('ban1w'))
async def bot_ban1w(message: types.Message):
    await bot_ban_x(message, seconds=604800)


@dp.message_handler(Command('ban1m'))
async def bot_ban1m(message: types.Message):
    await bot_ban_x(message, seconds=2592000)
