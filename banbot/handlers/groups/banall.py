import asyncio
from datetime import timedelta
from django.utils import timezone
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from banbot.loader import dp, bot
from banbot.models import User, Chat



def sync_check_rights(admin_user):
    try:
        user = User.objects.get(chat_id=admin_user, can_ban_all=True)
        if user:
            chat_ids = Chat.objects.values_list('chat_id', flat=True)
            return set(chat_ids)
    except:
        return None


async def bot_banall_x(message: types.Message, seconds):
    length = timedelta(seconds=seconds)
    reply_user_id = message.reply_to_message.from_user.id
    admin_user = str(message.from_id)
    # Получение текущего времени с учетом часового пояса Django
    now = timezone.now()

    # Добавляем заданное количество секунд к текущему времени
    ban_until = now + length

    chat_ids = await asyncio.to_thread(sync_check_rights, admin_user)
    for chat_id in chat_ids:
        await bot.ban_chat_member(chat_id=chat_id, user_id=reply_user_id, until_date=ban_until)
        # await message.answer(f"Пользователь id{ reply_user_id } заблокирован.")
    #else:
    #    await message.answer("Вы не можете выполнять данную команду.")


@dp.message_handler(Command('banall1min'))
async def bot_banall1min(message: types.Message):
    await bot_banall_x(message, seconds=60)


@dp.message_handler(Command('banall1d'))
async def bot_banall1d(message: types.Message):
    await bot_banall_x(message, seconds=86400)


@dp.message_handler(Command('banall1w'))
async def bot_banall1w(message: types.Message):
    await bot_banall_x(message, seconds=604800)


@dp.message_handler(Command('banall1m'))
async def bot_banall1m(message: types.Message):
    await bot_banall_x(message, seconds=2592000)
