import asyncio
from datetime import timedelta
from django.utils import timezone
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from banbot.loader import dp, bot
from banbot.models import User, Chat


def sync_check_rights(admin_user):
    try:
        user = User.objects.get(chat_id=admin_user, can_basta=True)
        if user:
            chat_ids = Chat.objects.values_list('chat_id', flat=True)
            return set(chat_ids)
    except:
        return None


async def bot_basta_x(message: types.Message, seconds):
    length = timedelta(seconds=seconds)
    reply_user_id = message.reply_to_message.from_user.id
    admin_user = str(message.from_id)
    # Получение текущего времени с учетом часового пояса Django
    now = timezone.now()

    # Добавляем заданное количество секунд к текущему времени
    ban_until = now + length

    has_rights = await asyncio.to_thread(sync_check_rights, admin_user)

    chat_ids = await asyncio.to_thread(sync_check_rights, admin_user)
    for chat_id in chat_ids:
        await bot.ban_chat_member(chat_id=chat_id, user_id=reply_user_id, until_date=ban_until, revoke_messages=True)
        # await message.answer(f"Пользователь id{ reply_user_id } заблокирован.")
    #else:
    #    await message.answer("Вы не можете выполнять данную команду.")


async def bot_bastauser_x(message: types.Message, seconds):
    length = timedelta(seconds=seconds)
    reply_user_id = message.reply_to_message.from_user.id
    admin_user = str(message.from_id)
    args = message.get_args()
    await message.answer(f"{args}")

    # Получение текущего времени с учетом часового пояса Django
    now = timezone.now()

    # Добавляем заданное количество секунд к текущему времени
    ban_until = now + length

    #has_rights = await asyncio.to_thread(sync_check_rights, admin_user)

    #chat_ids = await asyncio.to_thread(sync_check_rights, admin_user)
    #for chat_id in chat_ids:
        #await bot.ban_chat_member(chat_id=chat_id, user_id=reply_user_id, until_date=ban_until, revoke_messages=True)
        # await message.answer(f"Пользователь id{ reply_user_id } заблокирован.")
    #else:
    #    await message.answer("Вы не можете выполнять данную команду.")


@dp.message_handler(Command('basta'))
async def bot_basta(message: types.Message):
    await bot_basta_x(message, seconds=1)


@dp.message_handler(Command('bastauser'))
async def bot_bastauser(message: types.Message):
    await bot_bastauser_x(message, seconds=1)
